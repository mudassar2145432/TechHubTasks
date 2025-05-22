 Serverless Image Processing Web App (Flask + AWS Lambda + S3)
This project allows users to upload an image through a web interface. The image is then processed by a serverless AWS Lambda function triggered by S3 — resizing it and adding a watermark — and finally returned to the user through the Flask web app.

 Features
Upload image via web page

Resize and watermark the image using Pillow

View both original and processed images

Download processed image

Clean & responsive UI (HTML + CSS + JS)

Serverless backend using AWS Lambda, S3, IAM

 Technologies & Services Used
 Frontend:
HTML5 + CSS3

Vanilla JavaScript

Responsive design using Flexbox

⚙️ Backend (Local App):
Python 3.10+

Flask (Web framework)

Pillow (Image processing)

☁️ AWS Services:
Amazon S3: Image storage & Lambda trigger

AWS Lambda: Image resizing and watermarking

IAM Role: Permissions for Lambda to access S3

(Optional): Lambda Layers for Pillow dependencies

 How It Works (Architecture)
User uploads an image via the Flask app

Flask app sends image to S3 bucket

S3 triggers a Lambda function

Lambda resizes and watermarks the image

Processed image is saved back to a separate folder in S3 (processed/)

Flask app fetches and displays the processed image


💻 How to Run This Locally
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/image-processor.git
cd image-processor
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Flask app
bash
Copy
Edit
python app.py
Open your browser and go to http://localhost:5000

 Deploying the Lambda Function
Follow these only if you're setting up the serverless image processing with AWS.

Create S3 bucket

One for uploading images

Create processed/ folder inside for output

Write Lambda function

Use Python + Pillow to process image

ZIP your function + dependencies or use Lambda Layer

Add trigger

In S3: Add event notification to trigger Lambda on upload

IAM Permissions

Give your Lambda role permissions to read/write from S3

 To Do / Future Ideas
Add drag-and-drop upload support

Add image format conversion (PNG → JPG)

Add grayscale or rotate filters

Make API version for frontend apps

