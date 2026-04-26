from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

API_KEY ="671d22e0e50c2586cfdd2635c481971fY"

locations = {
    "kanyakumari": {
        "display": "Kanyakumari",
        "api_city": "Kanyakumari"
    },
    "muttom": {
        "display": "Muttom",
        "api_city": "Nagercoil"
    },
    "sothavilai": {
        "display": "Sothavilai",
        "api_city": "Nagercoil"
    },
    "vivekananda": {
        "display": "Vivekananda Rock",
        "api_city": "Kanyakumari"
    },
    "thengapattinam": {
        "display": "Thengapattinam",
        "api_city": "Nagercoil"
    }
}
sample_weather = [
    {
        "temperature": "32°C",
        "humidity": "78%",
        "wind_speed": "18 km/h",
        "condition": "Partly Cloudy"
    },
    {
        "temperature": "38°C",
        "humidity": "45%",
        "wind_speed": "12 km/h",
        "condition": "Sunny"
    },
    {
        "temperature": "28°C",
        "humidity": "92%",
        "wind_speed": "25 km/h",
        "condition": "Heavy Rain"
    }
]
def get_weather(city, display_name):
   if not API_KEY:
    sample = random.choice(sample_weather)

    return {
        "location": display_name,
        "temperature": sample["temperature"],
        "humidity": sample["humidity"],
        "wind_speed": sample["wind_speed"],
        "condition": sample["condition"]
    }

   except Exception as e:
    sample = random.choice(sample_weather)

    return {
        "location": display_name,
        "temperature": sample["temperature"],
        "humidity": sample["humidity"],
        "wind_speed": sample["wind_speed"],
        "condition": sample["condition"]
    }
@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/<place>')
def weather_report(place):
    if place in locations:
        city = locations[place]["api_city"]
        display_name = locations[place]["display"]
        weather = get_weather(city, display_name)
        return render_template('weather.html', weather=weather, place=place)
    return "Location not found"

if __name__ == '__main__':
    app.run(debug=True)