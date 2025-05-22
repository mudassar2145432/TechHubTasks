from flask import Flask, request, render_template
from PIL import Image, ImageDraw, ImageFont
import io
import base64

app = Flask(__name__)

def process_image(file_stream):
    img = Image.open(file_stream).convert("RGB")
    img = img.resize((200, 200))

    draw = ImageDraw.Draw(img)
    watermark_text = "© BloomBot"
    font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = img.width - text_width - 10
    y = img.height - text_height - 10

    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255))

    output = io.BytesIO()
    img.save(output, format='JPEG')
    output.seek(0)
    return output

@app.route('/', methods=['GET', 'POST'])
def upload_and_process():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read original image bytes for base64 encoding
            original_bytes = file.read()
            original_b64 = base64.b64encode(original_bytes).decode('utf-8')
            original_img_data = f"data:image/jpeg;base64,{original_b64}"

            # Process image using original bytes stream again
            processed_image_io = process_image(io.BytesIO(original_bytes))
            processed_b64 = base64.b64encode(processed_image_io.read()).decode('utf-8')
            processed_img_data = f"data:image/jpeg;base64,{processed_b64}"

            return render_template('index.html',
                                   original_img=original_img_data,
                                   processed_img=processed_img_data)

    return render_template('index.html', original_img=None, processed_img=None)

if __name__ == '__main__':
    app.run(debug=True)
