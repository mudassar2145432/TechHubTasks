import json
import urllib.request
from datetime import datetime
import boto3
from decimal import Decimal
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    API_KEY = "0c93018dcd83063c5911c70beb9fac55"
    CITIES = ["Faisalabad", "Lahore", "Islamabad", "Karachi", "Multan", "Peshawar", "murree"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('WeatherData')

    results = []

    for city in CITIES:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            with urllib.request.urlopen(url) as response:
                response_data = response.read()
                data = json.loads(response_data)

            timezone_offset = data.get('timezone', 0)

            weather_data = {
                'location': city,
                'timestamp': str(datetime.utcnow()),
                'temperature': Decimal(str(data['main']['temp'])),
                'humidity': Decimal(str(data['main']['humidity'])),
                'description': data['weather'][0]['description'],
                'feels_like': Decimal(str(data['main']['feels_like'])),
                'temp_min': Decimal(str(data['main']['temp_min'])),
                'temp_max': Decimal(str(data['main']['temp_max'])),
                'pressure': Decimal(str(data['main']['pressure'])),
                'wind_speed': Decimal(str(data['wind']['speed'])) if 'wind' in data else None,
                'visibility': Decimal(str(data.get('visibility', 0))),
                'clouds': Decimal(str(data['clouds']['all'])) if 'clouds' in data else None,
                'sunrise': datetime.utcfromtimestamp(data['sys']['sunrise'] + timezone_offset).strftime('%I:%M:%S %p'),
                'sunset': datetime.utcfromtimestamp(data['sys']['sunset'] + timezone_offset).strftime('%I:%M:%S %p'),
                'latitude': Decimal(str(data['coord']['lat'])),
                'longitude': Decimal(str(data['coord']['lon']))
            }

            # Store in DynamoDB
            table.put_item(Item=weather_data)
            logger.info(f"Weather data saved for {city}: {weather_data}")
            results.append(weather_data)

        except Exception as e:
            logger.error(f"Error for city {city}: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps(results, default=str)
    }
