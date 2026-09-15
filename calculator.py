def ask_number():
    while True:
        number = input("~ Type a number : ")
        try:
            num = float(number)
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


def ask_operation(x, y):
    while True:
        print(
            "======================"
            "\n--- OPTIONS ---"
            "\n ADDITION = +"
            "\n SUBTRACTION = - "
            "\n MULTIPLICATION = *"
            "\n DIVISION = /"
            "\n===================="
        )
        operation = input("Type your choice : ").strip()
        if operation == "+":
            return addition(x, y)
        elif operation == "-":
            return subtraction(x, y)
        elif operation == "*":
            return multiplication(x, y)
        elif operation == "/":
            return division(x, y)
        else:
            print(operation, "is not an option!")


result = None


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
    choice = input("Type your choice : ").strip()
    if choice == "A" or choice == "a":
        num_one = ask_number()
        num_two = ask_number()
        result = ask_operation(num_one, num_two)
        if result is not None:
            print(result)
    elif choice == "B" or choice == "b":
        if result is not None:
            num_one = result
            num_two = ask_number()
            result = ask_operation(num_one, num_two)
            if result is not None:
                print(result)
        else:
            print("No previous result!")
    elif choice == "C" or choice == "c":
        break
    else:
        print(choice, "is not an option!")