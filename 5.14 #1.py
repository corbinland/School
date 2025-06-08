weekDay = {

    0: "Sunday",

    1: "Monday",

    2: "Tuesday",

    3: "Wednesday",

    4: "Thursday",

    5: "Friday",

    6: "saturday"

}



def is_valid(input_string):

    try:

        val = int(input_string)

        if val < 0 or val > 6:

            return False

        return True

    except ValueError:

        return False

        

day = input("Enter day number (0-6): ")

isValid = is_valid(day)

while not isValid:

    day = input("Invalid input. Enter day number (0-6): ")

    isValid = is_valid(day)

    

n = int(day)

    

print(weekDay[n])
