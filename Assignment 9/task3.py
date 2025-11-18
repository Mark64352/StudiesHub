from task1 import Elevator

class Building:
    def __init__(self, bottom, top, number_of_elevators):
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination):
        print("\nUsing elevator", elevator_number + 1)
        print()
        print("The elevator is currently at the ground floor 1.")
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination)

    def fire_alarm(self):
        print("\n----------------------------------------------------------------")
        print("\n! FIRE ALARM ACTIVATED - MOVING ALL ELEVATORS TO GROUND FLOOR !\n")
        print("-----------------------------------------------------------------\n")
        for i, elevator in enumerate(self.elevators):
            print("MOVING ELEVATOR", i + 1, "TO THE BOTTOM FLOOR")
            print()
            elevator.current_floor_status()
            elevator.go_to_floor(elevator.bottom)
            print()


b = Building(1, 10, 3)

b.run_elevator(0, 5)
b.run_elevator(1, 3)
b.run_elevator(2, 9)

b.fire_alarm()
