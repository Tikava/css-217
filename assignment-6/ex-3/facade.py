from adapter import API1WeatherAdapter, API2WeatherAdapter

class WeatherFacade:
    def __init__(self):
        self.adapters = {
            'api1': API1WeatherAdapter(),
            'api2': API2WeatherAdapter(),
        }

    def get_weather(self, location, api):
        if api in self.adapters:
            return self.adapters[api].get_weather(location)
        else:
            print("Unsupported API")
            return None