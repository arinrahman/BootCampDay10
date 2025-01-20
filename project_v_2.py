from project_v_1 import operation
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2


while True:
    if first_number is None:  # Ask for the first number only if starting a new calculation
        first_number = float(input("What's the first number?\n"))

    operation = input("+, -, *, / Pick an operation: \n")
    next_number = float(input("What's the next number?\n"))

    operations = {
        "+": add(1, 2),
        "-": subtract(1, 2),
        "/": divide(1, 2),
        "*": multiply(1, 2)
    }
    for k in operations:
        res= operations[operation]

    print(f"{first_number} {operation} {next_number} = {res}")

    resp = input(f"Type 'y' to continue calculating with {res}, or 'n' to start a new calculation:\n").lower()
    if resp == "y":
        first_number = res  # Use the result as the first number for the next calculation
    elif resp == "n":
        first_number = None  # Reset for a new calculation
    else:
        print("Invalid input. Exiting the program.")
        break
