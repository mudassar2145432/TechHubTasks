import boto3
import uuid
import json

polly = boto3.client('polly')
s3 = boto3.client('s3')
bucket_name = 'my-tts-audio-bucket22'  # Replace with your actual bucket

def lambda_handler(event, context):
    try:
        # Handle JSON body sent by API Gateway
        body = json.loads(event['body'])
        text = body.get('text', '')

        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No text provided'})
            }

        # Generate speech
        response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')
        
        # Generate unique file name
        file_name = f"audio_{uuid.uuid4()}.mp3"

        # Upload to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=response['AudioStream'].read(),
            ContentType='audio/mpeg'
        )

        # Create a public S3 URL (assuming object is publicly accessible)
        audio_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'audioUrl': audio_url})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
