import random
def main():
    while True:
        print("-------To guess number---------")
        lower = int(input("Enter the starting the number for the range :"))
        upper = int(input("Enter the ending the number for the range :"))
        if lower>upper:
            print("The range is invalid")
        guess_no = 0
        count = 0
        x = random.randint(lower,upper)
        while guess_no != x:
            guess_no = int (input(f"Enter a number between{lower} to {upper} :"))
            if guess_no<lower or guess_no>upper:
                print(f"Invalid number guess between{lower} and{upper}")
            elif guess_no>x:
                print(f" U guessed higher value try again ")
            elif guess_no<x:
                print(f" U guessed lower value try again")
            count += 1
        print("U guessed the number correct ")
        print("the number times u guessed is ",count)

main()