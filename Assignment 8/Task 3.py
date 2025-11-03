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

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

carnew = Car("ABC-123", 142, 60, 2000)

carnew.drive(1.5)

print("Travelled distance:", carnew.travelled_distance, "km")
