def ask_number():
    while True:
        number = input("~ Type a number : ")
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


def ask_operation():
    while True:
        print(
            "======================"
            "\n--- OPTIONS ---"
            "\n 1. ADDITION = +"
            "\n 2. SUBTRACTION = - "
            "\n 3. MULTIPLICATION = *"
            "\n 4. DIVISION = /"
            "\n===================="
        )
        operation = input("Type your choice : ")
        if operation == "+":
            return addition(num_one, num_two)
            break
        elif operation == "-":
            return subtraction(num_one, num_two)
            break
        elif operation == "*":
            return multiplication(num_one, num_two)
            break
        elif operation == "/":
            return division(num_one, num_two)
            break
        else:
            print(operation, "is not an option!")


while True:
    print(
        "-------CALCULATOR--------"
        "\n <====================>"
        "\n -- OPTIONS --"
        "\n A. START"
        "\n B. CONTINUE"
        "\n C. EXIT"
        "\n <====================>"
    )
    choice = input("Type your choice : ")
    if choice == "A":
        num_one = ask_number()
        num_two = ask_number()
        result = ask_operation()
        if result != None:
            print(result)
    elif choice == "B":
        num_one = result
        num_two = ask_number()
        result = ask_operation()
        if result != None:
            print(result)
    elif choice == "C":
        break
    else:
        print(choice, "is not an option!")
