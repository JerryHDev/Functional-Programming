#Jerry Huang
#Period 4

from random import *
def main():
    print("This program simulates the dice game Craps.")
    n = eval(input("Enter the number of games to simulate: "))
    wins, loses = simGame(n)
    printSummary(wins, loses, n)

def simGame(n):
    wins = loses = 0
    for i in range(n):
        initial_roll1 = randrange(1, 7)
        initial_roll2 = randrange(1, 7)
        initial_roll = initial_roll1 + initial_roll2
        if initial_roll == 2 or initial_roll == 3 or initial_roll == 12:
            loses = loses + 1
        else:
            if initial_roll == 7 or initial_roll == 11:
                wins = wins + 1
            else:
                second_roll1 = randrange(1, 7)
                second_roll2 = randrange(1, 7)
                second_roll = second_roll1 + second_roll2
                while second_roll != initial_roll and second_roll != 7:
                    second_roll1 = randrange(1, 7)
                    second_roll2 = randrange(1, 7)
                    second_roll = second_roll1 + second_roll2
                if second_roll == initial_roll:
                    wins = wins + 1
                else:
                    loses = loses + 1
            
    return wins, loses

def printSummary(wins, loses, n):
    prob = wins/n
    print("\nGames simulated:", n)
    print("The number of wins is: {0} ({1:0.1%})".format(wins, prob))

if __name__ == '__main__': main()
