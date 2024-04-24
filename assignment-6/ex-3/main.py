from facade import WeatherFacade

def main():
    facade = WeatherFacade()
    location = "Almaty"
    api = "api2"
    weather_data = facade.get_weather(location, api)
    if weather_data:
        print('Temp. info: ', weather_data.temp_info)
        print('Wind info: ', weather_data.wind_info)
        print('Humidity: ', weather_data.humidity)


if __name__ == '__main__':
    main()