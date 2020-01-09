from random import choice
 
rules = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
previous = ['rock', 'paper', 'scissors']
 
while True:
    human = input('\nchoose your weapon: ')
    computer = rules[choice(previous)]  
 
    if human in ('quit', 'exit'): break
 
    elif human in rules:
        previous.append(human)
        print('the computer played', computer, end='; ')
 
        if rules[computer] == human:  
            print('yay you win!')
        elif rules[human] == computer:  
            print('the computer beat you... :(')
        else: print("it's a tie!")
 
    else: print("that's not a valid choice")