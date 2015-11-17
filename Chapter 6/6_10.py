#Jerry Huang
#Period 3

def main():
    phrase = input("Enter a phrase: ")
    answer = acronym(phrase)
    print(answer, end="")

def acronym(phrase):
    myList = phrase.split(" ")
    listLength = len(myList)
    x = 0
    acro = ""
    for i in range(listLength):
        f_word = myList[x]
        f_letter = f_word[0].upper()
        x = x + 1
        acro = acro + str(f_letter)

    return acro

main()
