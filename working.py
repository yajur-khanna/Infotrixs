import requests

# Function to load favorite cities from a file
def load_favorite_cities():
    try:
        with open('favorite_cities.txt', 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Load favorite cities at the start of the script
favorite_cities = load_favorite_cities()

# Function to add a city to the list of favorites
def add_favorite_city(city):
    if city not in favorite_cities:
        favorite_cities.append(city)
        save_favorite_cities()

# Function to remove a city from the list of favorites
def remove_favorite_city(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        save_favorite_cities()

# Function to display the list of favorite cities
def show_favorite_cities():
    if favorite_cities:
        print("Your favorite cities:")
        for idx, city in enumerate(favorite_cities, 1):
            print(f"{idx}. {city}")
    else:
        print("You have no favorite cities.")

# Function to save the list of favorite cities to a file
def save_favorite_cities():
    with open('favorite_cities.txt', 'w') as file:
        file.write('\n'.join(favorite_cities))


# Rest of your code (from fetching weather data onwards) goes here

API_KEY = '37a6146b7dfb46a3b97132850230611'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

city = input("Enter a city name: ")

params = {
    'key': API_KEY,
    'q': city
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {city}: {data['current']['condition']['text']}")
else:
    print("Failed to fetch weather data.")

def get_weather(city):
    params = {
        'key': API_KEY,
        'q': city
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['current']['condition']['text']
    else:
        return "Failed to fetch weather data."
import time

# Function for auto-refreshing weather data
def auto_refresh_weather(city, refresh_interval):
    while True:
        weather = get_weather(city)
        print(f"Weather in {city}: {weather}")
        print(f"Next update in {refresh_interval} seconds...")
        time.sleep(refresh_interval)
while True:
    print("\nOptions for managing favorite cities:")
    print("1. Add a city to favorites")
    print("2. Remove a city from favorites")
    print("3. Show favorite cities")
    print("4. Exit")

    option = input("Choose an option (1/2/3/4): ")

    if option == '1':
        new_favorite_city = input("Enter a city to add to favorites: ")
        add_favorite_city(new_favorite_city)
        print(f"{new_favorite_city} has been added to your favorite cities.")
    elif option == '2':
        city_to_remove = input("Enter a city to remove from favorites: ")
        remove_favorite_city(city_to_remove)
        print(f"{city_to_remove} has been removed from your favorite cities.")
    elif option == '3':
        show_favorite_cities()
    elif option == '4':
        city_to_refresh = input("Enter a city for auto-refresh: ")
        refresh_interval = 30  # Set the refresh interval in seconds (e.g., 1800 seconds = 30 minutes)
        auto_refresh_weather(city_to_refresh, refresh_interval)


        break

