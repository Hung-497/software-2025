import requests

name = input("Enter your name: ")
request = "https://api.agify.io/?name=" + name

try:
    response = requests.get(request)
    print(response)
    if response.status_code == 200:
        json_response = response.json()
        print(f"Name: {json_response["name"]} is {json_response["age"]} years old")
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")