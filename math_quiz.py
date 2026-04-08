import random

score = 0
run = True

while (run):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    operation = random.choice(["+", "-", "*", "/", "%"])
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = round(num1 / num2, 2)
    else:
        answer = num1 % num2

    user_answer = input(f"What is {num1} {operation} {num2}? ")
    if user_answer == "quit":
        break
    if answer == float(user_answer):
        score += 1
    print(f"score = {score}")