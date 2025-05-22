# 🚀 Mass Email Sender using AWS Lambda, SES, and API Gateway

This project is a simple, elegant mass email distribution system built with a **serverless architecture**. It allows you to send HTML emails to multiple recipients from a beautiful web interface.

---

## 🛠️ Features

- Mass email sending via a secure backend
- Serverless architecture using AWS Lambda & SES
- Clean, responsive HTML frontend
- Real-time status updates and loading spinner
- Emails sent with both content and notification

---

## 🧰 Technologies & AWS Services Used

| Technology | Purpose |
|-----------|---------|
| **AWS Lambda** | Runs backend code to send emails |
| **Amazon SES** (Simple Email Service) | Sends emails to recipients |
| **Amazon SNS** (optional) | Sends notifications when emails are sent |
| **API Gateway** | Provides HTTPS endpoint for frontend |
| **IAM** | Role permissions for Lambda access |
| **HTML/CSS/JavaScript** | Frontend for user interaction |

---

## 🌐 How It Works

1. User enters an email subject and HTML message in the frontend.
2. On clicking **"Send Emails"**, it makes a `POST` request to an API Gateway endpoint.
3. API Gateway triggers a Lambda function.
4. Lambda:
   - Sends the email via Amazon SES to a list of predefined recipients.
   - (Optionally) sends a notification using Amazon SNS.
5. The frontend displays a success or error message with a loading spinner during processing.



## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mass-email-sender.git
cd mass-email-sender
2. Deploy AWS Backend
Make sure you have:

An AWS account

AWS CLI installed & configured

Email verified in Amazon SES (if in sandbox mode)

Steps:

Create a Lambda function

Attach an IAM Role with ses:SendEmail permission

Create an API Gateway REST API or HTTP API to trigger the Lambda

Set Lambda code to:

python
Copy
Edit
# Python Lambda (simplified)
import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    subject = event["subject"]
    message = event["message"]
    recipients = ["employee1@example.com", "employee2@example.com"]
    
    for email in recipients:
        ses.send_email(
            Source="youremail@yourdomain.com",
            Destination={"ToAddresses": [email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Html': {'Data': message}}
            }
        )
    return {"statusCode": 200, "body": "Emails sent!"}
Deploy the API Gateway endpoint and copy the invoke URL

3. Update Frontend
In script.js, replace the API URL with your real API Gateway endpoint:

javascript
Copy
Edit
fetch('https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/MassEmailSender', ...)
4. Run It Locally
Open index.html in a browser or host it with:

bash
Copy
Edit
python3 -m http.server  # or use VS Code Live Server
✅ Output
🎯 All employees get the email

✅ You get a confirmation email

🟢 Status appears on screen with a spinner

📌 Notes
SES Sandbox Mode only allows sending to verified email addresses.

To send to unverified recipients, request production access in SES.
