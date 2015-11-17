#Jerry Huang
#Period 4

from random import *
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(probA, probB, n)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of volleyball.")
    print("You will be prompted to enter the probability of Team A")
    print("and Team B to win a game, and then enter the number of")
    print("games to be simulated. Games are played to 15, but must")
    print("be won by at least 2 points.")

def getInputs():
    #gets the user's input on probability and number of games to simulate
    a = eval(input("What is the probability Team A win's a serve? "))
    b = eval(input("What is the probability Team B win's a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(probA, probB, n):
    #simulates an n number of volleyball games
    #returns the number of wins for Team A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simAGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simAGame(probA, probB):
    #simulates one game and determines who wins that game based on probability
    #service starts with Team A
    #returns the team scores for Team A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    #a and b are the scores for the current volleyball game
    #Returns True if game is over, Flase otherwise
    return (a >= 25 and (a - 2) >= b) or (b >= 25 and (b - 2)>= a)
def printSummary(winsA, winsB):
    #prints a summary of the game results
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Team A wins: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Team B wins: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
    

