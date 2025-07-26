
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

operator= int(input("Select an operation(1,2,3 or 4):"))


num1 =int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if operator == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif operator == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif operator == 3:
    print(num1, "*", num2, "=", mul(num1, num2))
else:
    print(num1, "/", num2, "=", div(num1, num2))