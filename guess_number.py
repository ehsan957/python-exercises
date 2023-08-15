import random

number = random.randint(1,100)
counter = 0
while True:
    user_entered_number = int(input("Enter your guess: "))
    counter += 1
    if user_entered_number>number:
        print("Your guess is greater than mine")
    elif user_entered_number<number:
        print("Your guess is smaller than mine")
    else:
        print("you win in round", counter)
        break