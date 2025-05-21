import cv2
import boto3
import uuid
import os
from datetime import datetime
from flask import Flask, render_template, Response, request, jsonify

# AWS Clients
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')

# AWS resources
collection_id = 'students'
attendance_table = dynamodb.Table('AttendanceRecords')
details_table = dynamodb.Table('StudentDetails')  # Fetch student names from here

# Flask setup
app = Flask(__name__)

# Open camera
cap = cv2.VideoCapture(0)

latest_frame = None  # To keep the latest captured frame globally

# Stream video feed
def gen():
    global latest_frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        latest_frame = frame.copy()  # Save latest frame for capture endpoint
        ret, jpeg = cv2.imencode('.jpg', frame)
        if ret:
            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    global latest_frame
    if latest_frame is None:
        return jsonify({"message": "❌ No frame available"}), 500

    # Encode frame to JPEG bytes
    ret, jpeg_image = cv2.imencode('.jpg', latest_frame)
    if not ret:
        return jsonify({"message": "❌ Failed to encode image"}), 500
    image_bytes = jpeg_image.tobytes()

    try:
        response = rekognition.search_faces_by_image(
            CollectionId=collection_id,
            Image={'Bytes': image_bytes},
            FaceMatchThreshold=85,
            MaxFaces=1
        )

        matches = response.get('FaceMatches', [])
        if matches:
            face = matches[0]['Face']
            student_id = face['ExternalImageId']
            print(f"🎯 Detected StudentID from Rekognition: {student_id}")

            # Fetch student name from StudentDetails table
            try:
                response = details_table.get_item(Key={'StudentID': student_id})
                if 'Item' in response:
                    student_name = response['Item']['StudentName']
                else:
                    print(f"❌ StudentID '{student_id}' not found in StudentDetails table.")
                    student_name = "Unknown"
            except Exception as e:
                print("❌ Error fetching student name:", e)
                student_name = "Unknown"

            # Get current date and time
            current_datetime = datetime.now()
            current_date = str(current_datetime.date())
            current_time = current_datetime.strftime("%H:%M:%S")
            current_day = current_datetime.strftime("%A")

            # Check if attendance for this student already exists for today
            response = attendance_table.get_item(
                Key={'StudentID': student_id, 'Date': current_date}
            )

            if 'Item' in response:
                # Attendance already marked today
                print(f"❌ {student_name}, you are already marked present for today.")
                return jsonify({"message": f"❌ {student_name}, you are already marked present for today."})

            else:
                # Save attendance if not already present for today
                attendance_table.put_item(
                    Item={
                        'StudentID': student_id,
                        'StudentName': student_name,
                        'Date': current_date,
                        'Time': current_time,
                        'Day': current_day,
                        'Status': 'Present'
                    }
                )
                print(f"✅ {student_name} marked Present.")
                return jsonify({"message": f"✅ {student_name} marked Present."})

        else:
            print("❌ No face detected in the image.")
            return jsonify({"message": "❌ No face detected in the image."})

    except rekognition.exceptions.InvalidParameterException as e:
        print(f"❌ Error: {e}")
        return jsonify({"message": f"❌ Error: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
