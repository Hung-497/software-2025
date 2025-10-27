import requests

name = input("Enter municipality name: ")

request = "https://api.openweathermap.org/data/2.5/weather?q=" + name + "&appid=4e4c1d062c85e567fcc320a5a5f03ce8&units=metric"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        desc = ",".join(item['description'] for item in json_response['weather'])
        print(f"Weather: {desc}")
        print(f"Temperature: {json_response["main"]["temp"]} Celcius")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")