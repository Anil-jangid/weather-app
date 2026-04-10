import requests

API_KEY = '59546df67a801cdc924cd05c83cb3dbe'

class WeatherNotification:
    def __init__(self, city):
        self.city = city
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def get_weather(self):
        params = {
            'q': self.city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def notify(self):
        weather_data = self.get_weather()
        if weather_data['cod'] == 200:
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            print(f'The temperature in {self.city} is {temp}°C with {description}.')
        else:
            print(f'City {self.city} not found.')

if __name__ == '__main__':
    city = input('Enter the city name: ')
    notification = WeatherNotification(city)
    notification.notify()