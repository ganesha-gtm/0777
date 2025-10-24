try:
a=float (input("enter first number:"))
b=float(input("enter second number:"))
print(f"addition:{a+b}")
print(f"substraction:{a-b}")
print(f"multiplication:{a*b}")
if b !=0:
print(division by zero is not allowed.")
except ValueError:
print("please enter valid numbers.")
