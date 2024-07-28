import requests

try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=35.6764&lon=139.65&appid=9d55cacb9eea4865b92a29a960e8dffc")
except:
    print("No internet")

response_json = response.json()

temp = response_json["main"]["temp"]
temp_min = response_json["main"]["temp_min"]
temp_max = response_json["main"]["temp_max"]
