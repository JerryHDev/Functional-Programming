#Jerry Huang
#Period 4

from random import *
def main():
    printIntro()
    x = eval(input("Enter the number of simulations to run: "))
    y = 0
    for i in range(x):
        rollList = simARoll()
        a = rollList[0]
        b = rollList[1]
        c = rollList[2]
        d = rollList[3]
        e = rollList[4]
        if a == b and b == c and c == d and d == e:
            y = y + 1
    printSummary(y, x)
    
def printIntro():
    #prints intro
    print("This program estimates the probability of rolling")
    print("five-of-a-kind in a single roll of five six-sided dice.")
    


def simARoll():
    #simulates one single roll
    myList = []
    for i in range(5):
        rollValue = randrange(1, 7)
        myList.append(rollValue)
    return myList
def printSummary(y, x):
    prob = y/x
    print("\nThe probability of rolling five-of-a-kind is {0:0.1%}".format(prob))

if __name__ == '__main__': main()
        
