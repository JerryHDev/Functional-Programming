#Jerry Huang
#Period 4

from random import *
def main():
    printIntro()
    n = eval(input("Enter the number of steps to talk in this random walk: "))
    x = eval(input("Enter the nunber of times to simulate this random walk: "))
    y = 0
    for i in range(x):
        end = simAWalk(n)
        y = y + end
    printEnd(y, x)

def printIntro():
    print("This program simulates a random walk")

def simAWalk(n):
    a = 0
    for i in range(n):
        if random() > 0.5:
            a = a + 1
        elif random() < 0.5:
            a = a - 1
    end = abs(a)
    return end

def printEnd(y, x):
    average = y/x
    print("\nOn average, you will end up {0} steps from the starting point".format(average))

main()
    
            

