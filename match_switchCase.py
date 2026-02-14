day = input("Please select your day: (1-2)")

try:
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case _:
            print("Wrong input entered")
except:
    print("Wrong input entered")