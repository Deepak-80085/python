def check(alphabet):
    con = ['a','e','i','o','u']
    for i in con:
        if(alphabet == i):
            print(f"Given alphabet {i} vowel ")
            break
    else:
        print("Consonant")

def main():
    alphabet = str(input("Enter a alphabet : "))
    check(alphabet)
main()