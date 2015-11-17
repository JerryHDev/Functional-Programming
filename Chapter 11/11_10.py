#Jerry Huang
#Period 4

from math import*
def main():
    print("This program finds all the prime numbers up to some limit n.")
    n = eval(input("Enter some value for n: "))

    startList = []
    for i in range(n - 1):
        startList.append(i+2)

    while startList != []:
        number = startList[0]
        if number == 2:
            prime = True
            index = startList.index(number)
            print(startList.pop(index), end = " ")
            for number2 in startList:
                if number2 % number == 0:
                    startList.remove(number2)

        else:
            x = 2
            while prime == True and x <= sqrt(number):
                if number % x == 0:
                    primte = False

                else:
                    x = x + 1
            if prime == True:
                index = startList.index(number)
                print(startList.pop(index), end = " ")
                for number2 in startList:
                    if number2 % number == 0:
                        startList.remove(number2)
main()
        
