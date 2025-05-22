from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import uuid
import os

# AWS Setup
rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# AWS resources
bucket_name = 'attendance-images-bucket22'
collection_id = 'students'
details_table = dynamodb.Table('StudentDetails')

app = Flask(__name__)
app.secret_key = 'secret123'  # for flash messages


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_id = request.form['student_id']
        photo = request.files['photo']

        if not student_name or not student_id or not photo:
            flash("All fields are required.", "error")
            return redirect(url_for('register'))

        # Save to a temp file
        temp_filename = f"{uuid.uuid4().hex}.jpg"
        photo_path = os.path.join('temp', temp_filename)
        os.makedirs('temp', exist_ok=True)
        photo.save(photo_path)

        # Upload to S3
        s3_key = f"students/{student_id}-{uuid.uuid4().hex}.jpg"
        with open(photo_path, 'rb') as image:
            s3.upload_fileobj(image, bucket_name, s3_key)
        os.remove(photo_path)

        # Index face in Rekognition
        rekognition.index_faces(
            CollectionId=collection_id,
            Image={'S3Object': {'Bucket': bucket_name, 'Name': s3_key}},
            ExternalImageId=student_id,
            DetectionAttributes=['DEFAULT']
        )

        # Save to DynamoDB
        details_table.put_item(
            Item={
                'StudentID': student_id,
                'StudentName': student_name
            }
        )

        flash("✅ Student registered successfully!", "success")
        return redirect(url_for('register'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
