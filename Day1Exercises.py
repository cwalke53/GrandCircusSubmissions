echo = input("Hello user, enter your name:")
print(echo)

number = int(input(f"Ok great {echo}! Enter your favorite number and we'll increase it by 1:"))
number_plusone = number + 1
print(f"Your new number is {number_plusone}!")
print("Great!")

number = float(input("Now enter your favorite number and were going to add .5:"))
number_pluspointfive = number + .5
print(f"Your number with .5 added to it equals {number_pluspointfive}")

print("Ok now provide 2 numbers and were going to add them together.")
first_number = float(input("Enter your first number:"))
second_number = float(input("Enter your second number::"))
print(f"The answer is {first_number + second_number}")

print("Next, provide 2 numbers and we will multiply them!")
multipy_firstnumber = float(input("Enter your first number:"))
multipy_secondnumber = float(input("Enter your second number:"))
print(f"The answer is {multipy_firstnumber * multipy_secondnumber}")

print("Finally, provide 2 numbers and we will divide them.")
divide_firstnumber = int(input("Enter your first number:"))
divide_secondnumber = int(input("Enter your second number:"))
print(f"When dividing the 2 numbers the answer we receive is {int(divide_firstnumber / divide_secondnumber)}")
print(("Well done! You've completed this task."))



