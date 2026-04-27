from flask import Flask, render_template
import requests
import random
import os

app = Flask(__name__)

# Secure API Key from Environment Variable
API_KEY = os.environ.get("API_KEY")

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

location_details = {
    "kanyakumari": {
        "phone": "+91 4652 246223",
        "tourist_spots": ["Kanyakumari Beach", "Thiruvalluvar Statue", "Sunrise Point"],
        "hotels": ["Hotel Sea View", "Sparsa Resort", "Tri Sea Hotel"],
        "shops": ["Seashell Stores", "Local Handicrafts", "Beach Market"]
    },
    "muttom": {
        "phone": "+91 4651 223344",
        "tourist_spots": ["Muttom Beach", "Muttom Lighthouse", "Cliff View"],
        "hotels": ["Muttom Seaside Stay", "Ocean Breeze Inn"],
        "shops": ["Fishing Market", "Snack Shops"]
    },
    "sothavilai": {
        "phone": "+91 4651 998877",
        "tourist_spots": ["Sothavilai Beach", "Children Park"],
        "hotels": ["Beach Resort", "Sunset Inn"],
        "shops": ["Local Tea Shops", "Seafood Stalls"]
    },
    "vivekananda": {
        "phone": "+91 4652 112233",
        "tourist_spots": ["Vivekananda Rock Memorial", "Ferry Service"],
        "hotels": ["Sea Shore Hotel", "Temple Bay"],
        "shops": ["Souvenir Shops", "Book Stores"]
    },
    "thengapattinam": {
        "phone": "+91 4651 554433",
        "tourist_spots": ["Thengapattinam Estuary", "Fishing Harbor"],
        "hotels": ["Coastal Residency", "Harbor Inn"],
        "shops": ["Fish Market", "General Stores"]
    }
}

fallback_conditions = [
    "Sunny",
    "Partly Cloudy",
    "Cloudy",
    "Light Rain",
    "Humid",
    "Windy",
    "Thunderstorms Nearby"
]

def get_random_weather(display_name):
    return {
        "location": display_name,
        "temperature": random.randint(28, 38),
        "humidity": random.randint(50, 90),
        "wind_speed": random.randint(8, 30),
        "condition": random.choice(fallback_conditions)
    }

def get_weather(city, display_name):
    if not API_KEY:
        return get_random_weather(display_name)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return get_random_weather(display_name)

        return {
            "location": display_name,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["description"].title()
        }

    except Exception:
        return get_random_weather(display_name)

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/<place>')
def weather_report(place):
    if place in locations:
        city = locations[place]["api_city"]
        display_name = locations[place]["display"]
        weather = get_weather(city, display_name)
        details = location_details.get(place, {})

        return render_template(
            'weather.html',
            weather=weather,
            place=place,
            details=details
        )

    return "Location not found"

if __name__ == '__main__':
    app.run(debug=True)