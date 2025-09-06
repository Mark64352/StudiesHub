import random

code3 = ""
code4 = ""

digit1 = random.randint(0,9)
digit2 = random.randint(0,9)
digit3 = random.randint(0,9)

digit1 = random.randint(1,6)
digit2 = random.randint(1,6)
digit3 = random.randint(1,6)
digit4 = random.randint(1,6)


code3 += str(digit1) + str(digit2) + str(digit3)
code4 += str(digit1) + str(digit2) + str(digit3) + str(digit4)

print(f"3 digit lock combination: {code3}")
print(f"4 digit lock combination: {code4}")

#we didnt go thru in the class an example of different command use like, import, and random.randint, this is impossible to learn without ai :(
#smething like this is not also even in the github materials lesson 2.