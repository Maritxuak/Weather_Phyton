import requests
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_state, temperature = get_weather(city)
        return render_template('index.html', weather_state=weather_state, temperature=temperature, city=city)
    else:
        return render_template('index.html', weather_state=None, temperature=None, city=None)

def get_weather(city):
    api_key = 'abdfc21d8402330612ca51c385be69cb'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    if 'main' in data:
        temperature = data['main']['temp']
    else:
        temperature = "Не найдено"
    if 'weather' in data and len(data['weather']) > 0 and 'main' in data['weather'][0]:
        weather_state = data['weather'][0]['main']
    else:
        weather_state = "Не найдено"
    return weather_state, temperature
if __name__ == '__main__':
    app.run(debug=True)
