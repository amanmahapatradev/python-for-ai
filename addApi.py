import requests

latitude = 54.25
longitude = 3.61

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temprature_2m"

response = requests.get(url)
data = response.json()

print(data)
print(response)
print(requests)
type(data)
data["current"]["temprature_2m"]

