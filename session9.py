import requests

api_key = "96f68aa0e73c4e9399d3b99d48846a57"

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q=London"
    f"&appid={api_key}"
    "&units=metric"
)

response = requests.get(url)
data = response.json()

print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Feels Like:", data["main"]["feels_like"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Weather:", data["weather"][0]["description"])
print("Wind Speed:", data["wind"]["speed"], "m/s")