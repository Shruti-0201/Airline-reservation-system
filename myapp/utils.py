from datetime import datetime  # Used to work with date and time
import requests                # Used to make API requests
import logging                 # Used to log messages (optional)
from decouple import config    # Used to securely load API key from .env file

API_KEY = config('AVIATION_API_KEY')

# a demo dictionary to convert city names to their IATA airport codes
CITY_TO_IATA = {
    "delhi": "DEL",
    "mumbai": "BOM",
    "bangalore": "BLR",
    "chennai": "MAA",
    "hyderabad": "HYD",
    "kolkata": "CCU",
    "goa": "GOI",
    "ahmedabad": "AMD",
    "pune": "PNQ",
    "kochi": "COK",
    "tirupati": "TIR",
    "jaipur": "JAI",
    
}

# Function to convert a city name (e.g., "delhi") into its IATA code(e.g., "DEL")
def city_to_iata(city_name):
    return CITY_TO_IATA.get(city_name.lower())  # Make sure city name is lowercase

# Function to get flight data between two airports
def get_flight_data(source, destination, departure_date=None, return_date=None):
    try:
        # API URL with source and destination IATA codes and your access key
        url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&dep_iata={source}&arr_iata={destination}"
        
        # Send GET request to the aviationstack API
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses like 404 or 500
        json_data = response.json()  # Convert the API response to Python dictionary

        # Check if data is present in the response
        if 'data' in json_data:
            flights = json_data['data']  # Extract list of flights

            # Filter flights by departure date if provided
            if departure_date:
                flights = [
                    f for f in flights
                    if f.get('departure', {}).get('scheduled', '').startswith(departure_date)
                ]

            # Remove duplicate flights using a set to keep unique flight numbers
            seen = set()
            unique_flights = []
            for f in flights:
                flight_number = f.get('flight', {}).get('iata')  # Get flight number
                if flight_number and flight_number not in seen:
                    seen.add(flight_number)
                    unique_flights.append(f)

            return unique_flights[:10]  # Return only the first 10 unique flights
        else:
            return []  # No data found in the response

    except Exception as e:
        # If API fails or network is down, print error and return default/mock data
        print(f"API fetch failed: {e}")
        return [{
            "flight": {"iata": "DEFAULT123"},  # Dummy flight number
            "departure": {"airport": "Default Airport", "scheduled": departure_date or ""},
            "arrival": {"airport": "Default Destination"},
            "status": "scheduled",  # Dummy status
        }]
