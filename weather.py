from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap 
import requests

weather = Flask(__name__)
bootstrap = Bootstrap(weather)



def get_weather(city_name, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
            "Temperature": data["main"]["temp"],
            "Description": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"]
        }
        return weather_info
    else:
        return None
    
@weather.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city']
        api_key = "6cf13588b57142f0c752e3831d138664"

        weather = get_weather(city_name, api_key)

        if weather:
            return render_template('index.html', weather=weather)
        else:
            error_message = "Não foi possível obter a previsão do tempo." 
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')
if __name__ == "__main__":
    weather.run(debug=True)