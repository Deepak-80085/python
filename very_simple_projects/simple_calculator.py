print("----SIMPLE CALCULATOR ---------")

while True: 
    x = input("Enter an operator [add +, sub -, multi *, div /, exit]: ")
    
    if x.lower() == 'exit':
        break 
    
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    match x:
        case '+':
            c = a + b
            print("-------------------")
            print(c)
            print("-------------------")
        case '-':
            c = a - b
            print("-------------------")
            print(c)
            print("-------------------")
        case '*':
            c = a * b
            print("-------------------")
            print(c)
            print("-------------------")
        case '/':
            if b != 0: 
                c = a / b
                print("-------------------")
                print(c)
                print("-------------------")
            else:
                print("Error:invalid divisor.")
        case _:
            print("Invalid operator. Please try again.")
