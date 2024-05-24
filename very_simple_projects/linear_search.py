def linear():
    a = []
    while True:
        try:
            n = int(input("Enter the number of elements for the array"))
            break
        except ValueError:
            pass
    for i in range(n):
        x =int(input("elements : "))
        a.append(x)
    print(a)
    return a



def indexValue():
    a = linear()
    index = int(input("Value of the index : "))
    print(a[index])

def numberValue():
    a = linear()
    number = int(input("Enter the number : "))
    if number in a:
        index = a.index(number)
    print(index)

def main():
    option = int(input("1] To the number from the index \n2] To the index from the number \n Enter the 1 or 2 : "))
    if option == 1:
        indexValue()
    elif option == 2:
        numberValue()
    else:
        pass

main()