#Jerry Huang (Haoming)
#Period 4

def main():
    sentence = input("Type a sentence: ")
    myList = sentence.split()
    number_words = len(myList)
    x = 0
    new_number_letters = 0
    for i in range(number_words):
        lettersineach_word = myList[x]
        number_letters= len(lettersineach_word)
        x = x + 1
        new_number_letters = number_letters + new_number_letters
    average = new_number_letters / number_words
    print(average)

main()
        
