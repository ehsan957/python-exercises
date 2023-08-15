import random
selection = ['rock','scissors', 'paper']
def match(opt1, opt2):
    if opt1 == 0:
        if opt2 == 1:
            return 0
        elif opt2 == 2:
            return 1
        else:
            return 2
    elif opt1 == 1:
        if opt2 == 1:
            return 2
        elif opt2 == 2:
            return 0
        else:
            return 1
    else:
        if opt2 == 1:
            return 1
        elif opt2 == 2:
            return 2
        else:
            return 0
        
while True:
    user_input = input("please show your hand: ")
    user_choice = selection.index(user_input)
    
    computer_choice = random.randint(0,2)
    print(selection[computer_choice])
    result = match(user_choice, computer_choice)
    if result == 0:
        print("You win")
        break
    elif result == 1:
        print("You lost")
        break
    else:
        print("You draw, try again")