import tkinter as tk
from PIL import Image, ImageTk
import requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title('Weather App')
        master.geometry('400x300')
        
        # Load weather icon
        self.weather_icon = Image.open('weather_icon.png')
        self.weather_icon = self.weather_icon.resize((50, 50), Image.ANTIALIAS)
        self.weather_icon = ImageTk.PhotoImage(self.weather_icon)

        # Create GUI elements
        self.icon_label = tk.Label(master, image=self.weather_icon)
        self.icon_label.pack()
        
        self.city_label = tk.Label(master, text='Enter City:')
        self.city_label.pack()

        self.city_entry = tk.Entry(master)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(master, text='Get Weather', command=self.get_weather)
        self.get_weather_button.pack()

        self.result_label = tk.Label(master, text='')
        self.result_label.pack()
        
    def get_weather(self):
        city = self.city_entry.get()
        api_key = 'your_api_key_here'  # Replace with your actual API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={{city}}&appid={{api_key}}&units=metric'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            self.result_label.config(text=f'Temperature: {{temperature}}°C\nDescription: {{weather_description}}')
        else:
            self.result_label.config(text='City not found!')

if __name__ == '__main__':
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()