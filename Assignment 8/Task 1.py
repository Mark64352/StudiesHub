class Car:
    def __init__(self, reg_num, max_speed, current_speed, travelled_distance):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

carnew = Car("ABC-123", 142, 0, 0)

print("Regristration number:", carnew.reg_num)
print("Maximum Speed:", carnew.max_speed, "km/h")
print("Current Speed:", carnew.current_speed, "km/h")
print("Travelled Distance:", carnew.travelled_distance, "km")