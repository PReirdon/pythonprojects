from random import randint

t = ['rock', 'paper', 'scissors' ]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("rock, paper, or scissors? ")
    if player == computer:
        print('its a tie!')
#when player picks rock
    elif player == 'rock':
        if computer == 'paper':
            print("computer wins! paper covers rock")
        else:
            print("you win! rock smashes scissors!")
#when player picks paper
    elif player == 'paper':
        if computer == 'rock':
            print('you win! paper covers rock.')
        else:
            print('computer wins! scissors cuts paper.')
#when player picks scissors
    elif player == "scissors":
        if computer == "rock":
            print("computer wins! rock smashes scissors")
        else:
            print('you win! scissors cuts paper.')
#when a invalid option is picked
    else:
        print('please make sure to pick rock, paper, or scissors, and to check spelling.')
#asks if they eant to play again
    playa = input("would you like to play again? yes or no ")
    if playa == "yes":
        player = False
        computer = t[randint(0,2)]
    else:
        print("thanks for playing!")
        player = True
