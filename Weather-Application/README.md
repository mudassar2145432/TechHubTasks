# 🌍 Real-Time Weather Dashboard

A fully responsive, real-time weather dashboard web application built using **HTML, CSS, and JavaScript**, with a backend powered by **AWS Lambda**, **DynamoDB**, and **API Gateway**. The app is deployed and publicly accessible via **Netlify**.

---

## 🚀 Features

- Dynamic weather data display (temperature, humidity, pressure, etc.)
- Interactive city dropdown to view specific weather details
- Weather icons change based on conditions (e.g. ☀️, 🌧️, 🌩️)
- Beautiful UI with transparent cards and responsive layout
- Fully serverless backend on AWS
- Hosted live via Netlify

---

## 🧱 Tech Stack

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript
- Hosted on Netlify

### Backend (AWS)
- **DynamoDB**: Stores weather data per city
- **AWS Lambda**: Retrieves weather data from DynamoDB
- **API Gateway**: Exposes the Lambda function as a RESTful API


🔧 How It Works
Weather data is stored in DynamoDB with fields like temperature, humidity, description, timestamp, etc.
A Lambda function reads from DynamoDB and returns city-wise weather data in JSON.
API Gateway provides a public HTTPS endpoint for the Lambda.
On page load, the frontend (index.html) fetches this data and displays it dynamically.
User can select different cities from the dropdown to view updated weather data—no page reload needed.


🛠️ Setup & Deployment Instructions
🔹 Backend (AWS)
Create DynamoDB Table:
Table name: WeatherData
Primary key: location (String)
Insert Sample Weather Data:
Use AWS Console or a script to add JSON entries for different cities.
Create Lambda Function:
Use Python or Node.js to scan data from DynamoDB.
Return JSON-formatted results.
Create API Gateway Endpoint
Create a REST API.
Connect it to your Lambda function using a GET method.
Enable CORS and deploy the API.
Copy the endpoint URL (used in the frontend).

