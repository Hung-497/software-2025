# # class Car:
# #     def __init__(self, license_plate,maximum_speed):
# #         self.travelled_distance = 0
# #         self.license_plate = license_plate
# #         self.maximum_speed = maximum_speed
# #         self.current_speed = 0
# #     def __str__(self):
# #         return(f"License plate: {self.license_plate}\n"
# #                 f"Maximum speed: {self.maximum_speed} km/h\n"
# #                 f"Current speed: {self.current_speed} km/h\n"
# #                 f"Travelled distance: {self.travelled_distance} km")
# #     def accelerate(self,change_speed):
# #         self.current_speed += change_speed
# #         if self.current_speed > self.maximum_speed:
# #             self.current_speed = self.maximum_speed
# #         if self.current_speed < 0:
# #             self.current_speed = 0
# #     def drive(self, hours):
# #         distance = hours * self.current_speed
# #         self.travelled_distance += distance
# # import random
# # class Race:
# #     def __init__(self,name, distance,cars):
# #         self.cars = cars
# #         self.name = name
# #         self.distance = distance
# #     def hour_passes(self):
# #         for car in self.cars:
# #             car.accelerate(random.randint(-10,15))
# #             car.drive(1)
# #     def print_status(self):
# #         print("Plate | Max Speed(km/h) | Current Speed(km/h) | Distance(km)")
# #         print("-" * 60)
# #         for car in self.cars:
# #             print(f"{car.license_plate:6}|{car.maximum_speed:17}|{car.current_speed:21}|{car.travelled_distance:12.1f}")
# #     def race_finished(self):
# #         for car in self.cars:
# #             if car.travelled_distance >= self.distance:
# #                 return True
# #         return False

# # class Publication:
# #     def __init__(self,name):
# #         self.name = name
# # class Book(Publication):    
# #     def __init__(self,name, author,page_count):
# #         super().__init__(name)
# #         self.author = author
# #         self.page_count = page_count
# #     def print_information(self):
# #         print( f"{self.name} by {self.author}, {self.page_count} pages")
# # class Magazine(Publication):
# #     def __init__(self,name, chief_editor):
# #         super().__init__(name)
# #         self.chief_editor = chief_editor
# #     def print_information(self):
# #         print( f"Magazine {self.name} edited by {self.chief_editor}")

# # class Car:
# #     def __init__(self, license_plate,maximum_speed):
# #         self.travelled_distance = 0
# #         self.license_plate = license_plate
# #         self.maximum_speed = maximum_speed
# #         self.current_speed = 0
# #     def __str__(self):
# #         return(f"License plate: {self.license_plate}\n"
# #                 f"Maximum speed: {self.maximum_speed} km/h\n"
# #                 f"Current speed: {self.current_speed} km/h\n"
# #                 f"Travelled distance: {self.travelled_distance} km")
# #     def accelerate(self,change_speed):
# #         self.current_speed += change_speed
# #         if self.current_speed > self.maximum_speed:
# #             self.current_speed = self.maximum_speed
# #         if self.current_speed < 0:
# #             self.current_speed = 0
# #     def drive(self, hours):
# #         distance = hours * self.current_speed
# #         self.travelled_distance += distance
# # class ElectricCar(Car):
# #     def __init__(self,license_plate,maximum_speed,battery_capacity):
# #         super().__init__(license_plate,maximum_speed)
# #         self.battery_capacity = battery_capacity
# # class GasolineCar(Car):
# #     def __init__(self,license_plate,maximum_speed,tank_volume):
# #         super().__init__(license_plate,maximum_speed)
# #         self.tank_volume = tank_volume

# # import json
# # import requests

# # request = "https://api.chucknorris.io/jokes/random"
# # try:
# #     response = requests.get(request)
# #     if response.status_code = 200:
# #         data = response.json()
# #         print(data["value"])
# # except requests.exceptions.RequestException as e:
# #     print("Error occurred:", e)

# # import json
# # import requests
# # input = input('Enter municipality name: ')
# # request = "https://api.openweathermap.org/data/2.5/weather?q=" + input + "&appid=a194be8c9b43a9b4761faefedc60d492&units=metric"
# # try:
# #     response = requests.get(request)
# #     if response.status_code == 200:
# #         data = response.json()
# #         print(data["weather"][0]["description"])
# #         print(data["main"]["temp"], "Celsius")
# # except requests.exceptions.RequestException as e:
# #     print("Error occurred:", e)

# from flask import Flask, Response
# import json
# app = Flask(__name__)
# @app.route('/prime_number/<number>')
# def is_prime(number):
#     try:
#         number = int(number)
#         if number < 2:
#             isprime = False
#         else:
#             isprime = True
#             for i in range(2, int(number ** 0.5) + 1):
#                 if number % i == 0:
#                     isprime = False
#                     break
#         response = {
#             "Number" : number,
#             "isPrime" : isprime,
#         }
#         return response
#     except ValueError:
#         response = {
#             "message": "Invalid number as addend",
#             "status": 400
#         }
#         json_response = json.dumps(response)
#         http_response = Response(response=json_response, status=400, mimetype="application/json")
#         return http_response
# @app.errorhandler(404)
# def page_not_found(error_code):
#     response = {
#         "message": "Invalid endpoint",
#         "status": 404
#     }
#     json_response = json.dumps(response)
#     http_response = Response(response=json_response, status=404, mimetype="application/json")
#     return http_response

# if __name__ == '__main__':
#     app.run(use_reloader=True, host='127.0.0.1', port=5000)