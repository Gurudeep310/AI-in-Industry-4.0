import random
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import Adafruit_DHT

# Initialize Firebase with your credentials
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-acquisition-from-a-raspi-default-rtdb.firebaseio.com/'  # Replace with your database URL
})

sensor = Adafruit_DHT.DHT11
pin = 21
humidity, temperature = Adafruit_DHT.read_retry(sensor,pin) 

while True:
    if humidity is not None and temperature is not None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        humidity = round(humidity, 2)
        # Create a dictionary with the data to update
        data = {
            "timestamp": timestamp,
            "temperature": int(temperature),
            "humidity": humidity
        }
        # Update the data in the Firebase Realtime Database
        ref = db.reference('/sensor_data')  # Replace with your database reference path
        ref.push(data)
        print(f"Timestamp: {timestamp}, Temperature: {int(temperature)}°C, Humidity: {humidity}% - Data updated in Firebase")
    else:
        print("Failed to get")
    time.sleep(300)