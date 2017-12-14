import random


gamesStats = {
        "wins": 0,
        "draws": 0,
        "loses": 0
    }


def createRandomInt():

    return random.randint(1, 50)


def game():
    randoInt = createRandomInt()
    print("The random number is:", randoInt)
    maxGuessLimit = 5
    guessTaken = 0





    while guessTaken <= maxGuessLimit:
        userGuess = int(input("Pick a number 1-50: "))


        if userGuess == randoInt:
            print("You Guessed correct")
            gamesStats['wins'] += 1

            break
        elif userGuess < randoInt:
            print("The number I am thinking of is higher")
            guessTaken += 1
            continue
        else:
            print("The number I am thinking of is lower")
            guessTaken += 1
            continue

    if guessTaken >= 5:
        gamesStats['loses'] += 1

    playAgain(gamesStats)

def playAgain(gameStats):

    print("Game Stats", gameStats)

    userInput = input("Would you like to play again? Y/n: ")

    if userInput.lower() != "y":
        print("Thank you for playing, bye")
    else:
        game()



game()