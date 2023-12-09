print("Hello from Faker!")

from pymongo import MongoClient
from faker import Faker
import uuid
import math

# Connect to MongoDB
client = MongoClient('mongodb://database:27017/')
db = client['cms']  # Replace 'your_database_name' with your actual database name

# Import your MongoDB models here
# Example:
# attention_collection = db['attention']
# garbage_station_collection = db['garbage_stations']
# parked_cars_collection = db['parked_cars']
# patrol_collection = db['patrol']

fake = Faker('zh_CN')  # Use Chinese locale for Shanghai

# Base coordinates for Shanghai
shanghai_latitude = 31.2304
shanghai_longitude = 121.4737

# Function to generate random coordinates within a given radius
def generate_random_coordinates(base_latitude, base_longitude, radius_in_km):
    radius_in_deg = radius_in_km / 111.32  # Approximate degrees per kilometer
    u = float(fake.random.uniform(0, 1))
    v = float(fake.random.uniform(0, 1))
    w = radius_in_deg * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    latitude = base_latitude + x
    longitude = base_longitude + y

    return {'latitude': latitude, 'longitude': longitude}

# Function to add fake data to the Attention collection
def add_fake_attention_data():
    fake_attention_data = []

    for _ in range(10):
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)  # Adjust the radius as needed
        fake_attention_data.append({
            'timestamp': fake.date_time_this_year(),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'attentionId': str(uuid.uuid4()),
            'name': fake.name(),
            'contact': fake.phone_number(),
            'emergencyContact': fake.phone_number(),
            'emergencyType': fake.word(),
            'note': fake.sentence(),
        })

    # Example:
    # attention_collection.insert_many(fake_attention_data)
    print('Fake attention data added:', fake_attention_data)

# Function to add fake data to the GarbageStation collection
def add_fake_garbage_station_data():
    fake_garbage_station_data = []

    for _ in range(5):
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)  # Adjust the radius as needed
        fake_garbage_station_data.append({
            'timestamp': fake.date_time_this_year(),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'stationId': str(uuid.uuid4()),
            'status': fake.random_element(['Active', 'Inactive']),
            'personInCharge': fake.name(),
            'note': fake.sentence(),
        })

    # Example:
    # garbage_station_collection.insert_many(fake_garbage_station_data)
    print('Fake garbage station data added:', fake_garbage_station_data)

# Function to add fake data to the ParkedCars collection
def add_fake_parked_cars_data():
    fake_parked_cars_data = []

    for _ in range(3):
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)  # Adjust the radius as needed
        fake_parked_cars_data.append({
            'timestamp': fake.date_time_this_year(),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'parkingLotId': str(uuid.uuid4()),
            'numberOfCars': fake.random_int(min=5, max=20),
        })

    # Example:
    # parked_cars_collection.insert_many(fake_parked_cars_data)
    print('Fake parked cars data added:', fake_parked_cars_data)

# Function to add fake data to the Patrol collection
def add_fake_patrol_data():
    fake_patrol_data = []

    for _ in range(8):
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)  # Adjust the radius as needed
        fake_patrol_data.append({
            'timestamp': fake.date_time_this_year(),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'officerId': str(uuid.uuid4()),
            'officerContact': fake.phone_number(),
        })

    # Example:
    # patrol_collection.insert_many(fake_patrol_data)
    print('Fake patrol data added:', fake_patrol_data)

# Call the functions to add fake data
add_fake_attention_data()
add_fake_garbage_station_data()
add_fake_parked_cars_data()
add_fake_patrol_data()