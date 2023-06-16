import requests
import json
import config #see below


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    if data.get("weather"):
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        tempc = round(temperature-273.15,2)
        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature} K")
        print(f"Temperature: {tempc} °C")

        print(f"Humidity: {humidity}%")
    else:
        print("Weather information not available for the specified city.")

# create a config.py file in this folder. Add your api key to it (api_key = XXX)
api_key = config.api_key
city = input("Enter the city name: ")
get_weather(api_key, city)
