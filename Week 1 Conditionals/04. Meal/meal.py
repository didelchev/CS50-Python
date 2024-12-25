def main():
    user_input = input("What time is it? ")

    time = convert(user_input)

    if time >= 7 and time <= 8:
        print ('breakfast time')
    if time >= 12 and time <= 13:
        print('lunch time')
    if time >= 18 and time <= 19:
        print('dinner time')

def convert(time):
    hours, mins = time.split(":")

    new_mins = float (mins) / 60

    return float(hours) + new_mins

if __name__ == "__main__":
    main()






# Breakfast - 7:00 - 8:00

# Lunch - 12:00 - 13:00

# Dinner - 18:00 - 19:00

# 1. Get user input - DONE
# 2. Get time - DONE
# 3. Convert hours to normal numbers
# 4. Check the timings
# 5. Print the type of meal
