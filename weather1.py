import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status code {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print("No weather data to display.")

def main():
    api_key = "6c6e23fe150820f5d8d6aac2f4f5c194"  
    location = input("Enter city or ZIP code: ")

    weather_data = get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
    