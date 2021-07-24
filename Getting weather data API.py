""" using openweathermaps.org weather API  dc265dd419f3b329cc2860ed884a5be5 """

import requests
from pprint import pprint

API_Key = 'dc265dd419f3b329cc2860ed884a5be5'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_key + city

weather_data = request.get(base_url).json()

pprint(weather_data)
