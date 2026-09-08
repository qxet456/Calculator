while True:
    num1 = input(" Type a number : ")  
    try: 
        n1 = int(num1)
        break                                        # First number input 
    except ValueError :                
        print (" Error ")

while True:
    num2 = input(" Type a number : ")  
    try: 
        n2 = int(num2)
        break                                       # Second number input 
    except ValueError :
        print (" Error ")
 
while True:
      op = input(" Type your operation : ")
      if op == "+":
        add = n1 + n2 
        print (add)
        break 
      elif op == "-":
        sub = n1 - n2 
        print (sub)
        break
      elif op == "*":                                # Operation 
        mul = n1 * n2 
        print (mul)
        break 
      elif op == "/":
        div = n1 / n2 
        print (div)
        break 
      else:
        print ("Error")