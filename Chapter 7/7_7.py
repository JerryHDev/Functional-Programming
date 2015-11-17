#Jerry Huang
#Period 4

def main():
    try:
        #gets the starting and ending time
        print("This program calculates the total babysitting bill.")
        start = input("Enter the starting time in the format HH:MM:AM/PM: ")
        end = input("Enter the ending time in the format HH:MM:AM/PM: ")

        #splits the start and end times
        start = start.split(":")
        end = end.split(":")

        
        #gets the minutes of the time when the babysitting starts
        if start[2] == "AM":
            startTime = int(start[0]) * 60 + int(start[1])
        elif start[2] == "PM":
            startTime = (int(start[0]) + 12) * 60 + int(start[1])

        #gets the minutes of the time when the babysitting stops
        if end[2] == "AM":
            endTime = int(end[0]) * 60 + int(end[1])
        elif end[2] == "PM":
            endTime = (int(end[0]) + 12) * 60 + int(end[1])
            
        #time in minutes when the rate drops to $1.75
        timeMark = 1260
        
        #checks for illogical end and start times
        if endTime <= startTime:
            print("An error occured, the end time cannot be before the start time.")
            

        #if babysitter works past 9 PM
        if endTime > timeMark:
            workTime = timeMark - startTime
            workCharge = (workTime/60) * 2.50
            overTime = endTime - timeMark
            overCharge = (overTime/60) * 1.75
            totalCharge = workCharge + overCharge

        #if ending time is before 9 PM
        elif endTime < timeMark:
            workTime = endTime - startTime
            workCharge = (workTime/60) * 2.50
            totalCharge = workCharge

        print("The total babysitting bill is ${0}".format(totalCharge))
    except:
        print("An error occured, please try again.")
        
main()
            
            
                
            
            
