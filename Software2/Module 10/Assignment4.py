import random
class Car:
    def __init__(self, license_plate: str, maximum_speed: float):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change:float):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours: float):
        tvld = hours * self.current_speed
        self.travelled_distance += tvld

class Race:
    def __init__(self, name, distance:float, cars: list):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
    def print_status(self):
        print(f"{'Plate'} {'Max(km/h)'} {'Speed(km/h)'} {'Distance(km)'}")
        print("-" * 50)
        for car in self.cars:
            print(f"{car.license_plate} {car.maximum_speed} {car.current_speed} {car.travelled_distance}")
    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)