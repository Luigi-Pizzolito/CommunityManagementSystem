import datetime
from pymongo import MongoClient
from faker import Faker
import uuid
import json
import math
import numpy as np

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']  # Replace 'your_database_name' with your actual database name

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


def add_fake_attention_data():
    fake_attention_data = []
    
    # Defining a list of selected attention types with their likelihoods
    attention_types = [
        ('Fire', 0.05),  # Likelihood 5%
        ('Medical Emergency', 0.15),  # Likelihood 15%
        ('Traffic Accident', 0.1),  # Likelihood 10%
        ('Crime', 0.1),  # Likelihood 10%
        ('Road Closure', 0.1),  # Likelihood 10%
        ('Public Safety Issue', 0.15),  # Likelihood 15%
        ('Utility Outage', 0.1),  # Likelihood 10%
        ('Environmental Hazard', 0.25)  # Likelihood 25%
    ]

    for _ in range(25000):  # Increase the number of generated data
        # Randomly selecting an event type based on defined likelihoods
        event_type = fake.random.choices([event[0] for event in attention_types], 
                                         [event[1] for event in attention_types])[0]

        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)
        fake_attention_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'attentionId': str(uuid.uuid4()),
            'name': fake.name(),
            'contact': fake.phone_number(),
            'emergencyContact': fake.phone_number(),
            'emergencyType': event_type,
            'note': fake.sentence(),
        })

    with open('fake_attention_data.json', 'w') as json_file:
        json.dump(fake_attention_data, json_file, indent=2)


# Function to add fake data to the GarbageStation collection
def add_fake_garbage_station_data():
    fake_garbage_station_data = []

    for _ in range(25000):  # Increase the number of generated data
        # Biasing the likelihood of station statuses
        status = fake.random.choices(['Full', 'Normal', 'Empty'], [0.2, 0.6, 0.2])[0]  # Adjust likelihoods as needed
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 10)  # 10km radius
        fake_garbage_station_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'stationId': str(uuid.uuid4()),
            'status': status,
            'personInCharge': fake.name(),
            'note': fake.sentence(),
        })

    with open('fake_garbage_station_data.json', 'w') as json_file:
        json.dump(fake_garbage_station_data, json_file, indent=2)


# Function to add fake data to the ParkedCars collection
def add_fake_parked_cars_data():
    fake_parked_cars_data = []

    # Generate normally distributed probabilities
    weights = np.random.normal(loc=0.5, scale=0.15, size=15)
    weights = np.clip(weights, 0, 1)  # Ensure probabilities are between 0 and 1
    weights = weights / np.sum(weights)  # Normalize to sum up to 1

    for _ in range(25000):  # Increase the number of generated data
        num_cars = fake.random.choices(range(5, 20), weights)[0]  # Adjusted probabilities for each number
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)
        fake_parked_cars_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'parkingLotId': str(uuid.uuid4()),
            'numberOfCars': num_cars,
        })

    with open('fake_parked_cars_data.json', 'w') as json_file:
        json.dump(fake_parked_cars_data, json_file, indent=2)



# Function to add fake data to the Patrol collection
def add_fake_patrol_data():
    fake_patrol_data = []

    for _ in range(2500):  # Increase the number of generated data
        # Biasing the likelihood of patrol frequency
        random_coordinates = generate_random_coordinates(shanghai_latitude, shanghai_longitude, 5)
        fake_patrol_data.append({
            'timestamp': fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            'coordinates': random_coordinates,
            'address': fake.address(),
            'officerId': str(uuid.uuid4()),
            'officerContact': fake.phone_number(),
        })

    with open('fake_patrol_data.json', 'w') as json_file:
        json.dump(fake_patrol_data, json_file, indent=2)
        
# Function to add biased fake data to the Census collection
def add_fake_census_data():
    fake_census_data = []
    permanent_residency = ['Yes', 'No']

    for _ in range(100000):  # Increase the number of generated data
        age = fake.random_int(min=18, max=80)
        employment_status = get_biased_employment_status(age)
        
        fake_census_data.append({
            'name': fake.name(),
            'age': age,
            'censusId': str(uuid.uuid4()),
            'phone': fake.phone_number(),
            'employmentStatus': employment_status,
            'permanentResidency': fake.random.choice(permanent_residency),
        })

    with open('fake_census_data.json', 'w') as json_file:
        json.dump(fake_census_data, json_file, indent=2)

# Helper function to get biased employment status based on age
def get_biased_employment_status(age):
    if age < 25:
        return fake.random.choice(['Student', 'Unemployed'])
    elif 25 <= age <= 65:
        return fake.random.choice(['Employed', 'Unemployed', 'Student'])
    else:
        return fake.random.choice(['Retired', 'Employed'])

# Call the function to add fake census data
add_fake_census_data()


# Call the functions to add fake data
#add_fake_attention_data()
#add_fake_garbage_station_data()
#add_fake_parked_cars_data()
#add_fake_patrol_data()
