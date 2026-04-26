from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("671d22e0e50c2586cfdd2635c481971fY")

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

def get_weather(city, display_name):
    if not API_KEY:
        return {
            "location": display_name,
            "temperature": "N/A",
            "humidity": "N/A",
            "wind_speed": "N/A",
            "condition": "API key missing"
        }

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return {
                "location": display_name,
                "temperature": "N/A",
                "humidity": "N/A",
                "wind_speed": "N/A",
                "condition": data.get("message", "Weather unavailable")
            }

        return {
            "location": display_name,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["description"]
        }

    except Exception as e:
        return {
            "location": display_name,
            "temperature": "N/A",
            "humidity": "N/A",
            "wind_speed": "N/A",
            "condition": f"Error: {str(e)}"
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