from random import randint
from time import time
RPS = ['rock','paper','scissor']
computer = RPS[randint(0,2)]
player = False
while player == False :
    player = input('Please enter rock,paper,scissor ')
    if (player == computer):
        print('Its a Tie')
    elif player == 'rock':
        if computer == 'paper':
           print("Computer choosed ",computer,"And you choosed ",player)
           print('Computer WINS!')  
        else:
            print("Computer choosed ",computer,"And you choosed ",player)
            print('You WIN!')
    elif player == 'paper' :
        if computer == 'scissor' :
            print("Computer choosed ",computer,"And you choosed ",player)
            print('Computer WINS!')
        else:
            print("Computer choosed ",computer,"And you choosed ",player)
            print('You WIN!')
    elif player == 'scissor' :
        if computer == 'rock' :
            print("Computer choosed ",computer,"And you choosed ",player)
            print('Computer WINS!')
        else :
            print("Computer choosed ",computer,"And you choosed ",player)
            print('You WIN!')
    else :
        print('This is not a valid Move Please check the spelling!')
    player = False
    computer = RPS[randint(0,2)]