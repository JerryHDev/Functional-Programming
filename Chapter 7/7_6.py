#Jerry Huang
#Period 4

def main():

    try:
        speedLimit = eval(input("Enter the speed limit: "))
        clockedSpeed = eval(input("Enter the clocked speed: "))
        if clockedSpeed < speedLimit:
            print("The speed was legal.")
        if clockedSpeed > speedLimit:
            if clockedSpeed > 90:
                speedOver = (clockedSpeed - speedLimit) * 5
                ticket = speedOver + 50 + 200
                print("Your fine is $" + str(ticket))
            else:
                speedOver = (clockedSpeed - speedLimit) * 5
                ticket = speedOver + 50
                print("Your fine is $" + str(ticket))
    except:
        print("An error has occured... please try again.")
        
main()
            
