import re
from flask import Flask, jsonify, request
from http.client import responses
import requests

app = Flask(__name__)

@app.route('/city/<name>',methods=['GET'])
def task4(name):
  try:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "fb725cc2dc004d6ab823186d2c27fab1"
    # upadting the URL
    URL_APOD = BASE_URL + "q=" + name + "&units=metric&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL_APOD).json()
    print(response)
    dic={'country':response['sys']['country'],'name':response['name'],'temp':response['main']['temp'],'minimum temperature':response['main']['temp_min'],'maximum temperature':response['main']['temp_max'],
       'feels like':response['main']['feels_like'],'Type':response['weather'][0]['description']
    }
    return dic
  except:
    js={
    "status": 404,
    "message": "weather data not found"
    }
    return js

if __name__=="__main__":
    app.run(debug=True)