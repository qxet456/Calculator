while True:
    print ("OPTIONS : A for Calculation and B for Exit.")
    choice = input("Type your choice : ") 
    if choice == "A":
        def number():
            while True:
                num = input("Type a number :")
                try:
                    x = float(num)
                    return(x)
                except ValueError:
                    print("ERROR")
        n1 = number()
        n2 = number()
        def calculation(a,b):
            while True:
                op = input("Type your operation :")
                if op == "+":
                    add = a + b 
                    return(add)
                elif op == "-":
                    sub = a - b 
                    return(sub)
                elif op == "*":
                    mul = a * b 
                    return(mul)
                elif op == "/":
                    if b == 0:
                        return("CANNOT DIVIDE BY ZERO")
                    else:
                        div = a / b 
                        rem = a % b 
                        return(div,rem)
                else:
                    print("ERROR")
        result = calculation(n1,n2)
        print(result)
    elif choice == "B":
        break
    else:
        print("ERROR")