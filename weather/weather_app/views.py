import requests
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import WeatherForm
from .models import Weather
from django.conf import settings 

def weather_view(request):
    api_key = settings.API_KEY
    print(api_key)
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('city_weather')
        
    else:
        if Weather.objects.count()==0:
            city='Montreal'
        else:
            city = str(Weather.objects.latest('id'))

        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        response = requests.get(api_url)
        data = response.json()
        if len(data)==2 :
            if data['cod']=='404':
                Weather.objects.latest('id').delete()
                messages.error(request,'city not found !')
                return redirect('city_weather')
            
        temperature = convertTemp(data['main']['temp'])
        city = data['name']

        context = {
                'city': city,
                'temperature': temperature,
            }
        return render(request, 'weather.html', context)
    
def convertTemp(temp):
    return int (temp-273.15)
