import boto3
import os
from PIL import Image, ImageDraw, ImageFont
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key    = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    image_content = response['Body'].read()

    # Load image and convert to RGB (keep colors)
    img = Image.open(io.BytesIO(image_content)).convert("RGB")

    # Resize image to 200x200
    img = img.resize((200, 200))

    # Add watermark text
    draw = ImageDraw.Draw(img)
    watermark_text = "© WaterMark"

    # Use default font
    font = ImageFont.load_default()

    # Calculate watermark size
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Position watermark at bottom right with 10px padding
    x = img.width - text_width - 10
    y = img.height - text_height - 10

    # Draw white watermark text (RGB)
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255))

    # Save processed image to buffer as JPEG
    out_buffer = io.BytesIO()
    img.save(out_buffer, 'JPEG')
    out_buffer.seek(0)

    # Output key path
    out_key = f"processed/{os.path.splitext(os.path.basename(key))[0]}.jpg"

    # Upload processed image back to S3
    s3.put_object(Bucket=bucket, Key=out_key, Body=out_buffer.getvalue(), ContentType='image/jpeg')

    return {
        'statusCode': 200,
        'body': f"Processed and saved image as {out_key}"
    }
