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
1. Weather data is stored in DynamoDB with fields like temperature, humidity, description, timestamp, etc.
2. A Lambda function reads from DynamoDB and returns city-wise weather data in JSON.
3. API Gateway provides a public HTTPS endpoint for the Lambda.
4. On page load, the frontend (index.html) fetches this data and displays it dynamically.
5. User can select different cities from the dropdown to view updated weather data—no page reload needed.


🛠️ Setup & Deployment Instructions
🔹 Backend (AWS)
1. Create DynamoDB Table:
2. Table name: WeatherData
3. Primary key: location (String)
4. Insert Sample Weather Data:
5. Use AWS Console or a script to add JSON entries for different cities.
6. Create Lambda Function:
7. Use Python or Node.js to scan data from DynamoDB.
8. Return JSON-formatted results.
9. Create API Gateway Endpoint
10. Create a REST API.
11. Connect it to your Lambda function using a GET method.
12. Enable CORS and deploy the API.
Copy the endpoint URL (used in the frontend).

