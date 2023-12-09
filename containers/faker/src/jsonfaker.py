import datetime
from faker import Faker
import uuid
import json
import math

amount = 25000

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

    for _ in range(amount):  # Increase the number of generated data
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)
        fake_attention_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'attentionId': str(uuid.uuid4()),
            'name': fake.name(),
            'contact': fake.phone_number(),
            'emergencyContact': fake.phone_number(),
            'emergencyType': fake.word(),
            'note': fake.sentence(),
        })

    with open('json/fake_attention_data.json', 'w') as json_file:
        json.dump(fake_attention_data, json_file, indent=2)

# Function to add fake data to the GarbageStation collection
def add_fake_garbage_station_data():
    fake_garbage_station_data = []

    for _ in range(amount):  # Increase the number of generated data
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)
        fake_garbage_station_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'stationId': str(uuid.uuid4()),
            'status': fake.random_element(['Active', 'Inactive']),
            'personInCharge': fake.name(),
            'note': fake.sentence(),
        })

    with open('json/fake_garbage_station_data.json', 'w') as json_file:
        json.dump(fake_garbage_station_data, json_file, indent=2)

# Function to add fake data to the ParkedCars collection
def add_fake_parked_cars_data():
    fake_parked_cars_data = []

    for _ in range(amount):  # Increase the number of generated data
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)
        fake_parked_cars_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'parkingLotId': str(uuid.uuid4()),
            'numberOfCars': fake.random_int(min=5, max=20),
        })

    with open('json/fake_parked_cars_data.json', 'w') as json_file:
        json.dump(fake_parked_cars_data, json_file, indent=2)

# Function to add fake data to the Patrol collection
def add_fake_patrol_data():
    fake_patrol_data = []

    for _ in range(amount):  # Increase the number of generated data
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)
        fake_patrol_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'officerId': str(uuid.uuid4()),
            'officerContact': fake.phone_number(),
        })

    with open('json/fake_patrol_data.json', 'w') as json_file:
        json.dump(fake_patrol_data, json_file, indent=2)

add_fake_attention_data();
add_fake_garbage_station_data();
add_fake_parked_cars_data();
add_fake_patrol_data();