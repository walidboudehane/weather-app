# Weather App

## Description

The Weather App is a Django-based web application that provides real-time weather information for cities. It utilizes the OpenWeatherMap API to fetch weather data and allows users to save their favorite cities for quick access to weather updates.

## Features

- Display current temperature, city name, and weather condition.
- Allow users to save and manage their favorite cities.
- Provide error handling for invalid city names.
- Convert temperature units (default: Kelvin) for better user experience.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-weather-app.git
   cd your-weather-app
   
2.Install dependencies:

  ```bash
  pip install -r requirements.txt 
```

3.Set up the environment: 
    Create a virtual environment (optional but recommended).
    Copy .env.example to .env and add your OpenWeatherMap API key.

4.Run the application:

  ```bash
  python manage.py runserver
```

Access the app at http://localhost:8000.

License
This project is licensed under the MIT License.

