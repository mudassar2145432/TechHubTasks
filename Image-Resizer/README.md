#  Serverless Image Processing Web App (Flask + AWS Lambda + S3)

This project allows users to upload an image through a web interface. The image is then processed by a **serverless AWS Lambda function** triggered by S3 — resizing it and adding a watermark — and finally returned to the user through the Flask web app.

---

### Features

- Upload image via web page  
- Resize and watermark the image using **Pillow**
- View both **original and processed** images
- Download processed image
- Clean & responsive UI (HTML + CSS + JS)
- **Serverless backend** using AWS Lambda, S3, IAM

---

### Technologies & Services Used

###  Frontend:
- HTML5 + CSS3
- Vanilla JavaScript
- Responsive design using Flexbox

###  Backend (Local App):
- Python 3.10+
- Flask (Web framework)
- Pillow (Image processing)

###  AWS Services:
- **Amazon S3**: Image storage & Lambda trigger
- **AWS Lambda**: Image resizing and watermarking
- **IAM Role**: Permissions for Lambda to access S3
- **(Optional)**: Lambda Layers for Pillow dependencies

---

##  How It Works (Architecture)

1. User uploads an image via the Flask app  
2. Flask app sends image to S3 bucket  
3. S3 triggers a Lambda function  
4. Lambda resizes and watermarks the image  
5. Processed image is saved back to a `processed/` folder in S3  
6. Flask app fetches and displays the processed image  



##  How to Run This Locally

### 1. Clone the repo

```bash
git clone https://github.com/mudassar2145432/TechHubTasks/blob/main/Image-Resizer
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

Open your browser and go to `http://localhost:5000`

---

##  Deploying the Lambda Function

> Follow these if you're setting up the serverless processing on AWS.

1. **Create an S3 bucket**
   - Create `processed/` folder inside for output

2. **Write Lambda function**
   - Use Python + Pillow to process image
   - Package with dependencies or use a Lambda Layer

3. **Add trigger**
   - In S3: Add event notification to trigger Lambda on upload

4. **IAM Permissions**
   - Give Lambda role S3 read/write access

---

##  To Do / Future Ideas

- Drag-and-drop image upload
- Convert format (e.g., PNG → JPG)
- Add grayscale, rotate, or blur filters
- Build public API for developers

---

