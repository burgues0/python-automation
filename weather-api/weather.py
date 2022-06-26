import requests

API_KEY = "f3b6901576ea0d42dd0b9ef604d5723f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if(response.status_code == 200):
    data = response.json()
    print(data)
else:
    print("Error. No data retrieved.")