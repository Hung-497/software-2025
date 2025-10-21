class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Current floor: {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Current floor: {self.current_floor}")
    def go_to_floor(self, target: int):
        if target < self.bottom_floor:
            target = self.bottom_floor
        elif target > self.top_floor:
            target = self.top_floor
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor,top_floor) for _ in range(elevators)]
    def run_elevator(self, elevator_number, target):
        if 0 <= elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(target)