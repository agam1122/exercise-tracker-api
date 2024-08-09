# exercise-tracker-api

This repository contains a Python script that interacts with the Nutritionix and Sheety APIs to track exercises, log them, and manage workout data.


## Features

- **Fetch Exercise Data**: Collects exercise information from the Nutritionix API based on user input.
- **Log Workouts**: Logs exercise details (name, duration, calories burned) to Sheety.
- **Manage Workouts**: Retrieves current workout data and provides an example of deleting a specific workout entry.



## Setup

### Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library
- Nutritionix API credentials
- Sheety API credentials


### Installation

1. Clone the repository:
    ```
    git clone https://github.com/agam1122/exercise-tracker-api.git
    cd exercise-tracker-api
    ```
2. Install the required libraries:
    ```
    pip install requests requests
    pip install requests python-dotenv
    ```
3. Create a `.env` file in the root directory and add your Nutritionix API credentials:
    ```
    APP_ID=your_nutritionix_app_id
    API_KEY=your_nutritionix_api_key
    ```

    
### Usage

1. Run the script:
    ```
    python exercise_tracker.py
    ```
    or use any IDE of your choice

2. Follow the prompt to enter the exercises you did.


### Code Overview

- **Imports**: The script imports necessary libraries and modules (`requests`, `datetime`, `os`, `dotenv`).
- **Environment Variables**: Loads Nutritionix API credentials from a `.env` file.
- **Headers and Endpoints**: Defines headers and endpoints for Nutritionix and Sheety APIs.
- **User Input**: Prompts the user to input the exercises they did.
- **API Requests**: 
    - Makes a POST request to the Nutritionix API to fetch exercise data.
    - Makes a GET request to the Sheety API to retrieve current workout data.
    - Logs each exercise to Sheety using a POST request.
    - Provides an example of deleting a specific workout entry using a DELETE request.


- Ensure you replace placeholder values (`your_nutritionix_app_id`, `your_nutritionix_api_key`, `YOUR_AUTHENTICATION_TOKEN`) with actual credentials.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
