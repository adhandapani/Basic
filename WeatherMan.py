from flask import Flask, render_template, request
import requests

url="http://api.openweathermap.org/data/2.5/weather?APPID=f75a401594e632aecaca3498893c3290&q="
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/', methods=['POST'])
def calculate():

    City = request.form['city']
#    City = 'Chennai'
    FinalURL = url + City

    json_data = requests.get(FinalURL).json()
    display_data_weather = json_data['weather'] [0] ['description']
    display_data_wind = str(json_data['wind'] ['speed'])
    display_data_temp = str(json_data['main'] ['temp'])
    display_data_country = json_data['sys'] ['country']

    print("Weather      :" + display_data_weather)
    print("Wind Speed   :" + display_data_wind)
    print("Temparature  :" + display_data_temp)
    print("Country      :" + display_data_country)
#    return render_template('Output.html', a=display_data_weather,b=display_data_wind,c=display_data_temp,d=display_data_country)

    return render_template('Index.html', a=display_data_weather,b=display_data_wind,c=display_data_temp,d=display_data_country)

if __name__ == '__main__':
    app.run(debug=True)