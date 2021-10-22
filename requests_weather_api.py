import requests

resp = requests.get('https://goweather.herokuapp.com/weather/Berlin')
data = resp.json()
print(data["temperature"])
