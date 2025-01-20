resp = "y"
first_number = None  # Initialize first_number outside the loop

while True:
    if first_number is None:  # Ask for the first number only if starting a new calculation
        first_number = float(input("What's the first number?\n"))

    operation = input("+, -, *, / Pick an operation: \n")
    next_number = float(input("What's the next number?\n"))

    if operation == "+":
        res = first_number + next_number
    elif operation == "-":
        res = first_number - next_number
    elif operation == "/":
        if next_number == 0:
            print("Division by zero is not allowed.")
            continue
        res = first_number / next_number
    elif operation == "*":
        res = first_number * next_number
    else:
        print("Invalid operation. Please try again.")
        continue

    print(f"{first_number} {operation} {next_number} = {res}")

    resp = input(f"Type 'y' to continue calculating with {res}, or 'n' to start a new calculation:\n").lower()
    if resp == "y":
        first_number = res  # Use the result as the first number for the next calculation
    elif resp == "n":
        first_number = None  # Reset for a new calculation
    else:
        print("Invalid input. Exiting the program.")
        break
