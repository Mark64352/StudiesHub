#inputs
print("Enter three whole numbers (No decimals)") #print(f"Enter three whole numbers (No decimals)")
number1 = int(input("Enter whole number 1:"))
number2 = int(input("Enter whole number 2:"))
number3 = int(input("Enter whole number 3:"))

print()

print("Your numbers are " + str(number1) + "," + str(number2) + "," + str(number3) +".") #print(f"Your numbers are, {number1}, {number2}, {number3}.")

print()

#calculations
sum=number1+number2+number3
product=number1*number2*number3
average= sum/3

#results
print("The sum of the three whole numbers is", str(sum)+".") #print(f"The sum of three whole numbers is, {sum}.")
print("The product of the three whole numbers is", str(product)+".") #print(f"The product of the three whole numbers is, {product}.")
print("The average of the three whole numbers is", str(round(average, 2))+".") #print(f"The average of the three whole numbers is, {average}.")
