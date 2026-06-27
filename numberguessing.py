from random import randint

number = randint(1,100)

def attempt_5():
    attempt = 0
    while attempt < 5:
        guess_number = int(input("Guess a number (1-100) :"))
        attempt += 1
        if guess_number>100 or guess_number<1:
            print("Invalid input")

        elif guess_number > number: 
            print("Number is lower")

        elif guess_number < number:
            print("Number is higher")
        else:
            print(f"You Guessed a number in attempt {attempt}")
            break
    
    else:
        print(f"You lost! The number was {number}")

def attempt_10():
    attempt = 0
    while attempt < 10:
        guess_number = int(input("Guess a number (1-100) :"))
        attempt += 1
        if guess_number>100 or guess_number<1:
            print("Invalid input")

        elif guess_number > number: 
            print("Number is lower")

        elif guess_number < number:
            print("Number is higher")
        elif number == guess_number :
            print(f"You Guessed a number in attempt {attempt}")
            break
        else:
            print(f"You Guessed a number in attempt {attempt}")
            break
    
    else:
        print(f"You lost! The number was {number}")




print("1. 5 Attempts")
print("2. 10 Attempts")

menu_choice = int(input("Enter Your choice"))
if menu_choice==1:
    attempt_5()

elif menu_choice ==2:
    attempt_10
else:
    print("Enter valid input")
# while number != guess_number:
#     guess_number = int(input("Guess a number (1-100) :"))
#     attempt += 1

#     if guess_number>100 or guess_number<1:
#         print("Invalid input")

#     elif guess_number > number: 
#         print("Number is lower")

#     elif guess_number < number:
#         print("Number is higher")

#     else :
#         print(f"You Guessed a number in attempt {attempt}")