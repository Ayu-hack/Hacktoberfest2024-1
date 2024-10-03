#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# weather_app.py
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
    else:
        print("City not found.")

def main():
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()

