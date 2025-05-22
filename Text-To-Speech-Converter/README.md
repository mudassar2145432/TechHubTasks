#  Amazon Polly Text-to-Speech Web App

This is a simple Text-to-Speech (TTS) web application that converts user-input text into lifelike speech using Amazon Polly. The project uses AWS Lambda, Amazon S3, and Amazon API Gateway to perform text-to-audio conversion and serve the resulting audio on a beautifully styled HTML page.

---

## Features

- Convert custom text into speech using Amazon Polly
- Play generated audio directly in the browser
- Beautiful, responsive UI using HTML/CSS/JS
- Fully serverless — powered by AWS Lambda + API Gateway + S3

---

##  Technologies & Services Used

| Layer | Technology |
|-------|------------|
| Frontend | HTML5, CSS3 (Inter font, Responsive), JavaScript (Fetch API) |
| Backend | AWS Lambda (Python) |
| Storage | Amazon S3 (for storing and serving .mp3 files) |
| API Gateway | REST API to trigger Lambda |
| TTS Engine | Amazon Polly |

---

#  Amazon Polly Text-to-Speech Web App

This is a simple Text-to-Speech (TTS) web application that converts user-input text into lifelike speech using Amazon Polly. The project uses AWS Lambda, Amazon S3, and Amazon API Gateway to perform text-to-audio conversion and serve the resulting audio on a beautifully styled HTML page.

---

##  Features

- Convert custom text into speech using Amazon Polly
- Play generated audio directly in the browser
- Beautiful, responsive UI using HTML/CSS/JS
- Fully serverless — powered by AWS Lambda + API Gateway + S3

---

##  Technologies & Services Used

| Layer | Technology |
|-------|------------|
| Frontend | HTML5, CSS3 (Inter font, Responsive), JavaScript (Fetch API) |
| Backend | AWS Lambda (Python) |
| Storage | Amazon S3 (for storing and serving .mp3 files) |
| API Gateway | REST API to trigger Lambda |
| TTS Engine | Amazon Polly |

---

##  How It Works

1. User enters text in the browser UI.
2. The JavaScript sends a POST request to an AWS API Gateway endpoint.
3. The API Gateway triggers a Lambda function.
4. Lambda:
   - Converts text to speech using Amazon Polly.
   - Saves the audio file (.mp3) to Amazon S3.
   - Returns the public URL of the audio file.
5. The browser receives the audio URL and plays it in an embedded HTML5 audio player.

---

##  Setup & Run

### 1. Deploy AWS Lambda Function

- Go to AWS Lambda
- Create a new function (Python 3.9+)
- Add permissions to access Amazon Polly and S3
- Paste your code that:
  - Receives POST request with text
  - Uses Polly to synthesize speech
  - Uploads .mp3 to S3
  - Returns S3 audio URL as JSON

### 2. Configure API Gateway

- Create a REST API
- Create a POST method (e.g. /tts) pointing to the Lambda
- Enable CORS for the method
- Deploy the API and copy the endpoint URL

### 3. Update Frontend

In script.js, update the fetch() URL:

```js
fetch("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/tts",

Replace with your actual API Gateway endpoint.

4. Run the Frontend
You can:

Open index.html directly in your browser, or

Serve it with a static server (e.g., using Live Server in VSCode)




