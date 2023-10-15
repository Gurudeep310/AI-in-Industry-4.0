import random
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase with your credentials
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-acquisition-from-a-raspi-default-rtdb.firebaseio.com/'  # Replace with your database URL
})

# Define the range for temperature and humidity
min_temperature = 23
max_temperature = 25
min_humidity = 60
max_humidity = 70

while True:
    # Generate a random number to decide whether to fluctuate temperature
    fluctuate = random.random() < 0.05  # Adjust the probability as needed (e.g., 0.05 for 5% chance)
    
    if fluctuate:
        # Generate a slightly fluctuated temperature
        temperature = round(random.uniform(min_temperature - 0.5, max_temperature + 0.5), 0)
    else:
        # Generate a stable temperature
        temperature = round(random.uniform(min_temperature, max_temperature), 2)
    
    # Generate random humidity value
    humidity = round(random.uniform(min_humidity, max_humidity), 2)
    
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
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
    
    # Sleep for 5 minutes
    time.sleep(300)  # 300 seconds = 5 minutes
