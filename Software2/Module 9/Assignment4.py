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


def race():
    cars = [Car(f"ABC-{i}",random.randint(100,200)) for i in range(1,11)]
    while True:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
        if any(car.travelled_distance >= 10000 for car in cars):
            break
    cars.sort(key = lambda c: c.travelled_distance,reverse= True)
    return cars

