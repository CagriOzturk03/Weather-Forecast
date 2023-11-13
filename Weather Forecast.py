import requests

def get_weather_forecast(city, unit='metric'):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/onecall"
    params = {
        "q": city,
        "appid": api_key,
        "units": unit,
        "exclude": "current,minutely,daily",
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        print(f"Hourly Weather Forecast for {city}:")
        for hour in data['hourly']:
            print(f"Time: {hour['dt']}, Temperature: {hour['temp']} °{unit}, Weather: {hour['weather'][0]['description']}")
    elif response.status_code == 401:
        print("Invalid API key. Please check your API key.")
    elif response.status_code == 404:
        print(f"Weather data not found for {city}. Please enter a valid city name.")
    else:
        print("An error occurred. Please try again later.")

if __name__ == '__main__':
    print("Welcome to the Weather Forecast Application!")
    while True:
        city_name = input("Enter the city name (type 'exit' to quit): ")
        if city_name.lower() == 'exit':
            break
        unit_choice = input("Enter the unit you want the temperature to be displayed in (metric/imperial) [Default is metric]: ")
        unit = unit_choice if unit_choice in ['metric', 'imperial'] else 'metric'
        get_weather_forecast(city_name, unit)
