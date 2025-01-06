# Get user input

# Split user input into - day, month, year

# Prompt the user for input

# Convert the user input

# Print the user input

months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def get_user_input():
    while True:
        date = input('Date:').strip()
        try:
            month, day, year = date.split("/")
            if int(day) <= 31 and int(day) >= 1 and int(month) >= 1 and int(month) <= 12:
                print(f'{year}-{int(month):02}-{int(day):02}')
                break
        except:
            try:
                old_month, old_day, year = date.split(" ")
                if old_month in months:
                    month = months[old_month]
                    if not old_day.endswith(","):
                        continue
                    else:
                        day = old_day.strip(",")
                        if int(day) <= 31 and int(day) >= 1 and int(month) >= 1 and int(month) <= 12:
                            print(f'{year}-{int(month):02}-{int(day):02}')
                            break
            except:
                pass





get_user_input()



#September 9, 1920
