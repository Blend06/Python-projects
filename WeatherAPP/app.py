import requests

api_key = '40f16178b7d6d03b82017567b2f3dcfc'

user_input = input("Enter city name: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is {weather} and the temperature is {temp}°F.")
