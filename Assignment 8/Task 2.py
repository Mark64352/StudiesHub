class Car:
    def __init__(self, reg_num, max_speed, current_speed, travelled_distance):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        elif self.current_speed < 0:
            self.current_speed = 0

carnew = Car("ABC-123", 142, 0, 0)

carnew.accelerate(30)
carnew.accelerate(70)
carnew.accelerate(50)
print("Current speed:", carnew.current_speed, "km/h")

carnew.accelerate(-200)
print("Final speed:", carnew.current_speed, "km/h")
