from utils import Fetcher
from config import config
from weather import WeatherTarget

class WeatherAdapter:
    def get_weather(self, location):
        pass
    
class API1WeatherAdapter(WeatherAdapter):
    
    def __init__(self):
        self.fetcher = Fetcher(url="https://api.weatherapi.com/v1/current.json")
        
    def get_weather(self, location):
        data = self.fetcher.make_get_request(params=dict(q=location, key=f'{config.WEATHERAPI_KEY}'))
        if data:
            return WeatherTarget(
                temp_info=dict(
                    feels_like=dict(celsius=data['current']['feelslike_c'], fahrenheit=data['current']['feelslike_f']),
                    temp=dict(celsius=data['current']['temp_c'], fahrenheit=data['current']['temp_f'])
                    ),
                wind_info=dict(
                    wind_degree=data['current']['wind_degree'], 
                    wind_speed=data['current']['wind_kph']
                    ),
                humidity=data['current']['humidity']
            )
            
        return None
    
class API2WeatherAdapter(WeatherAdapter):
    
    def __init__(self):
        self.fetcher = Fetcher(url="https://api.openweathermap.org/data/2.5/weather")
    
    def get_weather(self, location):
        data = self.fetcher.make_get_request(params=dict(q=location, appid=f"{config.OPENWEATHER_KEY}"))
        if data:
            return WeatherTarget(
                temp_info=dict(
                    feels_like=dict(
                        celsius=round(data['main']['feels_like'] - 273, 1),
                        fahrenheit=round((data['main']['feels_like'] - 273) * 1.8 + 32, 1)
                    ),
                    temp=dict(
                        celsius=round(data['main']['temp'] - 273, 1),
                        fahrenheit=round((data['main']['temp'] - 273) * 1.8 + 32, 1)
                    )
                ),
                wind_info=dict(
                    wind_degree=data['wind']['deg'],
                    wind_speed=round(data['wind']['speed'] * 3.6, 1)
                ),
                humidity=data['main']['humidity']
            )

        return None
