def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero"
    return a / b

print("Simple Calculator")
a = float(input("First number: "))
b = float(input("Second number: "))
operation = input("Operation (add/subtract/multiply/divide): ")

if operation == "add":
    print(add(a, b))
elif operation == "subtract":
    print(subtract(a, b))
elif operation == "multiply":
    print(multiply(a, b))
elif operation == "divide":
    print(divide(a, b))
else:
    print("Unknown operation")