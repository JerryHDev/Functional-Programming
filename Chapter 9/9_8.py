#Jerry Huang
#Period 4

from random import *
def main():
    print("This program simulates a game of blackjack and predicts the probability the dealer will bust.")
    a = getInputs()
    wins, losses = simAGames(a)
    printResults(a, wins, losses)

def getInputs():
    a = eval(input("How many games of blackjack do you want to simulate? "))
    return a

def simAGames(a):
    #simulates a number of games
    wins = 0
    losses = 0
    for i in range(a):
        score = simGame()
        if score <= 21:
            wins = wins + 1
        else:
            losses = losses + 1
    return wins, losses

def simGame():
    score = 0
    while not gameOver(score):
        card, hasAce = drawCard()
        if card == "ace" and hasAce == True:
            if score >= 6 and score <= 10:
                score = score + 11
            else:
                score = score + 1
        else:
            score = score + card
    return score

def drawCard():
    card = randrange(1, 14)
    if card == 1:
        return "ace", True
    elif card == 11 or card == 12 or card == 13:
        return 10, False
    else:
        return card, False

def gameOver(score):
    return (score >= 17 and score <= 21) or score >= 22

def printResults(a, wins, losses):
    print("\nGames simulated:", a)
    print("Number of wins: {0}".format(wins))
    print("Number of busts: {0}".format(losses))

main()
