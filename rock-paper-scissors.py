#Quira Cordero
#Python - Rock, Paper, Scissors 
#09/22/2023
#CISW 24L


import random, sys

print("EXPELLIAMUS, PROTEGO, SECTUMSEMPRA")

"""
This game is based on Harry Potter Spells. 
ROCK represents EXPELLIARMUS: It's a disarming spell that knocks a victim's 
weapon (usually a wand) out of his/her hands. 
PAPER represents PROTEGO: It's a spell used to guard its caster from incoming spells
SCISSORS represents SECTUMSEMPRA: It's a curse that causes brutal lacerations 
on the target's body as if they've been slashed with an invisible blade.
"""

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:  # The player input loop.
        print("Enter your move: (e)xpelliarmus (p)rotegi (s)sectumsempra or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()  # Quit the program.
        if playerMove == "e" or playerMove == "p" or playerMove == "s":
            break  # Break out of the player input loop.
        print("Type one of e, p, s, or q.")

    # Display what the player chose:
    if playerMove == "e":
        print("EXPELLIARMUS versus...")
    elif playerMove == "p":
        print("PROTEGO versus...")
    elif playerMove == "s":
        print("SECTUMSEMPRA versus...")

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "e"
        print("EXPELLIARMUS")
    elif randomNumber == 2:
        computerMove = "p"
        print("PROTEGO")
    elif randomNumber == 3:
        computerMove = "s"
        print("SECTUMSEMPRA")

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
    elif playerMove == "e" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "e":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "e" and computerMove == "p":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "e":
        print("You lose!")
        losses = losses + 1
