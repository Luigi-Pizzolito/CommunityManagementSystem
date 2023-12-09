print("Hello from Faker!")

import datetime
from pymongo import MongoClient
from faker import Faker
import uuid
import time
from pymongo.errors import ServerSelectionTimeoutError

# Connect to MongoDB
max_retries = 30

def connect_to_mongodb():
    for _ in range(max_retries):
        try:
            client = MongoClient('mongodb://admin:RqHLLWROgV3htvxRJXRJJilPDDq9sMejOMt9ovOYoNpKpsNC6hSCtCFxqHql1UQw@localhost:27017/', serverSelectionTimeoutMS=1000)
            client.server_info()
            return client
        except ServerSelectionTimeoutError:
            print("Waiting for MongoDB to be ready...")
            time.sleep(1)
    raise Exception("Failed to connect to MongoDB")

client = connect_to_mongodb()
db = client['cms']

# Create collections
attention_collection = db.create_collection('attention')
garbage_station_collection = db.create_collection('garbage_station')
parked_cars_collection = db.create_collection('parked_cars')
patrol_collection = db.create_collection('patrol')

# Faker instance for generating fake data
fake = Faker('zh_CN')

# Sample data for each collection with coordinates and addresses
attention_data = {
    'timestamp': datetime.datetime.now(),
    'location': 'Shanghai, China',
    'attentionId': str(uuid.uuid4()),
    'name': fake.name(),
    'contact': fake.phone_number(),
    'emergencyContact': fake.phone_number(),
    'emergencyType': fake.word(),
    'note': fake.sentence(),
}

garbage_station_data = {
    'timestamp': datetime.datetime.now(),
    'location': 'Shanghai, China',
    'stationId': str(uuid.uuid4()),
    'status': fake.random_element(['Active', 'Inactive']),
    'personInCharge': fake.name(),
    'note': fake.sentence(),
}

parked_cars_data = {
    'timestamp': datetime.datetime.now(),
    'location': 'Shanghai, China',
    'parkingLotId': str(uuid.uuid4()),
    'numberOfCars': fake.random_int(min=5, max=20),
}

patrol_data = {
    'timestamp': datetime.datetime.now(),
    'location': 'Shanghai, China',
    'officerId': str(uuid.uuid4()),
    'officerContact': fake.phone_number(),
}

# Insert sample data into the respective collections
attention_collection.insert_one(attention_data)
garbage_station_collection.insert_one(garbage_station_data)
parked_cars_collection.insert_one(parked_cars_data)
patrol_collection.insert_one(patrol_data)

print("Sample data inserted successfully.")
