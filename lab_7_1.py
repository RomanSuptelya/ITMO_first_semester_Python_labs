
import json
import requests

city_name = "Saint Petersburg"
key = ""
response = requests.get (f"https://api.openweathermap.org/data/2.5/weather?"
                         f"q={city_name}&appid={key}")
result = json.loads(response.text)
#print(result)

# Извлечение данных
temperature_kelvin = result['main']['temp']
weather_description = result['weather'][0]['description']
humidity = result['main']['humidity']
pressure_hpa = result['main']['pressure']

# Преобразование давления в мм рт. ст.
pressure_mm_rt_st = round(pressure_hpa * 0.750062)
# Преобразование температуры из Кельвинов в градусы Цельсия
temperature_celsius = round(temperature_kelvin - 273.15)

# Вывод результатов
print(f"Температура: {temperature_celsius}°C")
print(f"Погода: {weather_description}")
print(f"Влажность: {humidity}%")
print(f"Давление: {pressure_mm_rt_st}(мм рт. ст.)")