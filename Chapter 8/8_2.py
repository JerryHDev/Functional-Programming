#Jerry Huang
#Period 4

def main():
    print("This program prints a nicely formatted table of windchill values.")
    print("")


    #makes the row for the wind speed
    windSpeed = 0
    print(end = "    ")
    for i in range(11):
        print("{0:>6}".format(windSpeed), end = "")
        windSpeed = windSpeed + 5

    #makes the column for temperatures and the windChill values
    temperature = -20
    windSpeed = 0
    print("")
    for i in range(9):
        List = []
        print("")
        for i in range(11):
            List.append(windChill(windSpeed, temperature))
            windSpeed = windSpeed + 5
        print("{0:>6} {1:>5} {2:>5.2f} {3:>5.2f} {4:>5.2f} {5:>5.2f} {6:>5.2f} {7:>5.2f} {8:>5.2f} {9:>5.2f} {10:>5.2f}".format(temperature, "N/A", List[1], List[2], List[3], List[4], List[5], List[6], List[7], List[8], List[9], List[10]))
        temperature = temperature + 10


def windChill(V,T):
    windchill = 35.74 + (0.62157 * T) - (35.75 * (V**0.16)) + (0.4275 * T * (V**0.16))
    return windchill

    
        
main()
        
