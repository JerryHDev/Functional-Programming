#Jerry Huang (Haoming)
#Period 4

#main function gets the name
def main():
    full_name = input("Enter your first and last name: ")
    full_name = full_name.lower()
    full_namelist = full_name.split(" ")
    length = len(full_namelist)
    x = 0
    total = 0

    #cycles through the first and last name
    for i in range(length):
        word = full_namelist[x]
        word_length = len(word)
        x = x + 1
        y = 0
        
        #cycles through the letters of each name
        for i in range(word_length):
            letter = word[y]
            value = ord(letter) - 96
            total = total + value
            y = y + 1

    print(total)
main()
        
        
