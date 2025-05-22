import boto3
import json

ses = boto3.client('ses', region_name='us-east-1')
sns = boto3.client('sns', region_name='us-east-1')

def lambda_handler(event, context):
    # Parse data from HTML request
    body = json.loads(event['body'])
    subject = body.get('subject', 'No Subject')
    body_html = body.get('message', '<p>No content provided.</p>')

    # Email list
    emails = ["alikhanhojaega@gmail.com", "elikhann692@gmail.com"]

    for email in emails:
        ses.send_email(
            Source="harrybittering123@gmail.com",
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Html': {'Data': body_html}}
            }
        )

    # Send SNS notification
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:585008077700:MassEmailNotifications',
        Message=f"Mass email sent to {len(emails)} recipients.",
        Subject="Mass Email Notification"
    )

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps('Emails sent and notification published!')
    }
