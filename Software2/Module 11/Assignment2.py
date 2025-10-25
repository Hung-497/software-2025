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

class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, bettery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = bettery_capacity

class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume