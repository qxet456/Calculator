while True:
    print ("OPTIONS : 1 for Calculation and 2 for Exit.")
    choice = input("Type your choice : ")
    try: 
        a = int(choice)
        if a == 1:
            while True:
                num1 = input("Type a number :")
                try:
                    n1 = float(num1)
                    break
                except ValueError:
                    print("ERROR")
            while True:               
                num2 = input("Type a number :")
                try:
                    n2 = float(num2)
                    break
                except ValueError:
                    print("ERROR")
            while True:
                op = input("Type your operation :")
                if op == "+":
                    add = n1 + n2 
                    print(add)
                    break
                elif op == "-":
                    sub = n1 - n2 
                    print(sub)
                    break
                elif op == "*":
                    mul = n1 * n2 
                    print(mul)
                    break
                elif op == "/":
                    if n2 == 0:
                        print("CANNOT DIVIDE BY ZERO")
                    else:
                        div = n1 / n2 
                        rem = n1 % n2
                        print(div,rem)
                        break
                else:
                    print("ERROR")
        elif a == 2:
            break
        else:
            print ("ERROR")
    except ValueError:
        print ("ERROR") 