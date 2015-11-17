#Jerry Huang
#Period 4

def main():
    phrase = input("Enter a phrase: ")
    myList = phrase.split(" ")
    listLength = len(myList)
    x = 0
    for i in range(listLength):
        f_word = myList[x]
        f_letter = f_word[0].upper()
        print(f_letter, end="")
        x = x + 1

main()
