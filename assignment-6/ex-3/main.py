import requests

from config import config

#first api

url = "https://api.weatherapi.com/v1/current.json"
res = requests.get(url=url, params=dict(q='Almaty', key=f'{config.WEATHERAPI_KEY}')).json()
print(res['location']['name'])



#second api

url = "https://api.openweathermap.org/data/2.5/weather"
res = requests.get(url=url, params=dict(appid=f"{config.OPENWEATHER_KEY}", q='Almaty')).json()
print(res['name'])