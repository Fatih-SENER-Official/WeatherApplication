import requests
import tkinter
from tkinter import messagebox

# Create the main window

window = tkinter.Tk()
window.title("Weather Application")
window.minsize(width=400, height=300)
window.config(padx=20,pady=20)

# Create and configure labels and entry fields

city_label = tkinter.Label(window, text="City:")
city_label.pack()
city_entry = tkinter.Entry(window)
city_entry.pack()

# Create a button to fetch weather data
fetch_button = tkinter.Button(window, text="Fetch Weather")
fetch_button.pack()

# Create a label to display weather information
weather_label = tkinter.Label(window, text="")
weather_label.pack()

# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    # Add your API key here
    api_key = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

fetch_button.config(command= fetch_weather)



window.mainloop()