import requests  # Import requests to handle HTTP requests
from datetime import datetime  # Import datetime to handle date and time operations
import os  # Import os to access environment variables
from dotenv import load_dotenv  # Import dotenv to load environment variables from a .env file

# Load environment variables from a .env file
load_dotenv()

# Retrieve Nutritionix API credentials from environment variables
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

# Headers for Nutritionix API requests
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

# Base URL and endpoints for Nutritionix API
HOST_DOMAIN = "https://trackapi.nutritionix.com"
nutrients_endpoint = "v2/natural/nutrients"
instant_endpoint = "v2/search/instant"
exercise_endpoint = "v2/natural/exercise"


# Collect user input for the exercises they performed
parameters = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 77,  # User's weight in kilograms
    "height_cm": 170,  # User's height in centimeters
    "age": 20  # User's age
}

# Send a POST request to Nutritionix API to get exercise data
response = requests.post(url=f"{HOST_DOMAIN}/{exercise_endpoint}", json=parameters, headers=headers)
data = response.json()  # Parse the response JSON
print(data)  # Print the exercise data

# (Commented out) Example of how to make a GET request to the instant search endpoint
# response1 = requests.get(url=f"{HOST_DOMAIN}/{instant_endpoint}", params=parameters, headers=headers)
# print(response1.text)


# Make a GET request to Sheety API to retrieve the current workout data
response2 = requests.get(url="https://api.sheety.co/5af3340df06fa407cc4e37c5a986467c/myWorkouts/sheet1")
data2 = response2.json()  # Parse the response to JSON
print(data2)  # Print the current workout data


# Get the current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%H:%M:%S")

# Log each exercise to Sheety
for exercise in data["exercises"]:
    # Prepare the data for each exercise
    parameters = {
        'sheet1': {
                'date': today_date,
                'time': today_time,
                'exercise': exercise["name"].title(),
                'duration': exercise["duration_min"],
                'calories': exercise["nf_calories"]
            }
    }

    # Headers for Sheety API requests
    headers = {
        "Content-Type": "application/json",
        "Authorization": "YOUR_AUTHENTICATION_TOKEN"
    }
    # Make a POST request to Sheety API to log the exercise
    response3 = requests.post(url="https://api.sheety.co/5af3340df06fa407cc4e37c5a986467c/myWorkouts/sheet1",
                              json=parameters, headers=headers)
    # Print the response from Sheety
    print(response3.json())


# Example of how to delete a specific workout entry from Sheety (entry with ID 2)
requests.delete(url=f"https://api.sheety.co/5af3340df06fa407cc4e37c5a986467c/myWorkouts/sheet1/2")




