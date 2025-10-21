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
        print("Plate | Max Speed(km/h) | Current Speed(km/h) | Distance(km)")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.license_plate:6}|{car.maximum_speed:17}|{car.current_speed:21}|{car.travelled_distance:12.1f}")
    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

cars = []
for i in range(1, 11):
    license_plate = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    car = Car(license_plate, maximum_speed)
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\nStatus after {hours} hours:")
        race.print_status()

print(f"\nRace finished after {hours} hours!")
print("Final results:")
race.print_status()