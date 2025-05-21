# Real-Time Face Recognition Attendance System

A complete guide and documentation for implementing a real-time face recognition attendance system using Python (Flask) and AWS services.

---

## Overview

This project is a web-based biometric attendance system that uses a webcam to capture student faces and logs their attendance based on facial recognition. The system leverages AWS Rekognition to identify faces and AWS DynamoDB to store attendance records.

---

## Technologies and Services Used

### Backend Technologies

* **Python 3.x**
* **Flask** (Web Framework)
* **OpenCV** (For accessing the webcam)
* **Boto3** (AWS SDK for Python)

### AWS Services

* **Amazon Rekognition** - For facial recognition and face matching
* **Amazon DynamoDB** - To store student details and attendance records
* **Amazon S3** (Optional) - Temporarily used for image uploads
* **IAM Roles** - For permissions to access AWS services

---

## Project Structure

```
attendance-face-recognition/
├── app.py                    # Main Flask application
├── templates/
│   └── index.html            # Frontend UI
├── static/
│   ├── preview.mp3           # Success audio
│   ├── error.mp3             # Error audio
│   └── logo.png              # Institute logo (optional)
├── requirements.txt          # Python dependencies
```

---

## Steps to Set Up the Project

### Step 1: Clone the Repository

```
git clone https://github.com/yourusername/attendance-face-recognition.git
cd attendance-face-recognition
```

### Step 2: Create and Activate Virtual Environment

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install Required Python Packages

```
pip install -r requirements.txt
```

### Step 4: Configure AWS Credentials

Make sure your AWS CLI is configured properly:

```
aws configure
```

Enter your AWS Access Key, Secret Key, Region, and Output format.

### Step 5: Create Rekognition Collection

```
aws rekognition create-collection --collection-id students
```

### Step 6: Index Student Faces to Rekognition

Use a script or AWS CLI to index each student's image:

```
aws rekognition index-faces \
  --collection-id students \
  --image "S3Object={Bucket=your-bucket,Name=path/to/image.jpg}" \
  --external-image-id "StudentID123" \
  --detection-attributes "ALL"
```

*Alternatively, modify your own Python script to upload and index images.*

### Step 7: Create DynamoDB Tables

#### Table 1: StudentDetails

* **Primary Key**: `StudentID` (String)
* Attributes: `StudentName`

#### Table 2: AttendanceRecords

* **Primary Key**: `StudentID` (String)
* **Sort Key**: `Date` (String)
* Other Attributes: `StudentName`, `Time`, `Day`, `Status`

### Step 8: Run Flask App

```
python app.py
```

Open your browser and go to:

```
http://localhost:5000
```

---

## How It Works

1. The application accesses the webcam and streams the video.
2. When the user clicks "Mark Attendance", the current frame is captured.
3. The image is sent to AWS Rekognition (without storing in S3).
4. Rekognition searches the collection for a matching face.
5. If a face match is found:

   * The StudentID is extracted.
   * The StudentName is retrieved from `StudentDetails`.
   * Today's attendance is checked in `AttendanceRecords`.
   * If not marked, it adds the record; else shows already present.
6. A modal popup displays the result and plays audio feedback.

---

## User Interface

* Responsive and centered UI
* Embedded live video stream
* One-click attendance capture
* Feedback via modal popup and audio
* Optional top-left institute logo

---

## Future Improvements

* Admin dashboard for viewing records
* Email/SMS notification integration
* Deploy to AWS EC2 or Elastic Beanstalk
* Multi-user role-based access control

---



---

## Acknowledgments

* [OpenCV](https://opencv.org/)
* [Flask](https://flask.palletsprojects.com/)
* [AWS Rekognition](https://aws.amazon.com/rekognition/)
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/)
