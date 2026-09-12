def ask_number():
    while True:
        number = input("~ Type a number :")
        try:
            num = int(number)
            return num
        except ValueError:
            print("Type a number!")


def addition(a, b):
    add = a + b
    return add


def subtraction(a, b):
    sub = a - b
    return sub


def multiplication(a, b):
    mul = a * b
    return mul


def division(a, b):
    if b == 0:
        print("Can't divide by zero!")
    else:
        div = a / b
        return div


def operation():
    print(
        "===================="
        "\n--- OPTIONS ---"
        "\n 1. ADDITION = +"
        "\n 2. SUBTRACTION = - "
        "\n 3. MULTIPLICATION = *"
        "\n 4. DIVISION = /"
        "\n===================="
    )
    operation = input("Type your choice : ")
    if operation == "+":
        addition(num_one, num_two)
        return addition(num_one, num_two)
    elif operation == "-":
        subtraction(num_one, num_two)
        return subtraction(num_one, num_two)
    elif operation == "*":
        multiplication(num_one, num_two)
        return multiplication(num_one, num_two)
    elif operation == "/":
        division(num_one, num_two)
        return division(num_one, num_two)
    else:
        print(operation, "is not an option!")


while True:
    print(
        "<====================>"
        "\n -- OPTIONS --"
        "\n A. CALCULATOR"
        "\n B. EXIT"
        "\n <====================>"
    )
    choice = input("Type your choice : ")
    if choice == "A":
        num_one = ask_number()
        num_two = ask_number()
        result = operation()
        print(result)
    elif choice == "B":
        break
    else:
        print(choice, "is not an option!")
