from flask import Flask, render_template
import requests

app = Flask(__name__)

# Your Weather API Key
API_KEY = "your_api_key_here"

# Kanyakumari coastal locations
locations = {
    "kanyakumari": "Kanyakumari",
    "muttom": "Muttom",
    "sothavilai": "Sothavilai",
    "vivekananda": "Vivekananda Rock Memorial",
    "thengapattinam": "Thengapattinam"
}

# Function to fetch weather
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = {
        "location": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["description"]
    }

    return weather

# Home page
@app.route('/')
def home():
    return render_template('index.html', locations=locations)

# Dynamic route for each coastal place
@app.route('/<place>')
def weather_report(place):
    if place in locations:
        weather = get_weather(locations[place])
        return render_template('weather.html', weather=weather)
    else:
        return "Location not found"

# Run app
if __name__ == '__main__':
    app.run(debug=True)