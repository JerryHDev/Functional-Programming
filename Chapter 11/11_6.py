#Jerry Huang
#Period 4

from random import *
def main():
    print("This program scrambles a list into a random order.")
    x = input("Enter a list of objects separated by a comma: ")
    myList = x.split(",")
    newList = shuffle(myList)
    print(newList)

def shuffle(myList):
    length = len(myList)
    newList = []
    for i in range(length):
        x = randrange(0, length)
        newList.append(myList[x])
        del myList[x]
        length = length - 1
    return newList

main()
