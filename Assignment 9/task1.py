class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor += 1
        print("The elevator is now at floor", self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print("The elevator is now at floor", self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

    def current_floor_status(self):
        if self.current_floor == self.bottom:
            print("The elevator is now at the ground floor.")
        else:
            print("The elevator is now at floor", self.current_floor)

if __name__ == "__main__":
    h = Elevator(1, 10)
    h.current_floor_status()
    h.go_to_floor(5)
    h.go_to_floor(1)
