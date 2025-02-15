# [] Get User Input - age, weight, height, activity ?
# [] Calculate TDEE
# [] Option to loose weight
# [] Option to gain weight 
# [] Option to maintain weight


def main():
    get_user_input()



def get_user_input():
    age = input('Age:')
    weight = input('Weight:')
    height = input('Height:')
    activity = {
        "Sedentary (little to no exercise)": int(1.2),
        "Light exercise (1-3 days per week)": int(1.375),
        "Moderate exercise (3-5 days per week)" : int(1.55),
        "Heavy exercise (6-7 days per week)" : int(1.725),
        "Very heavy exercise (Twice per day,intense)" :int(1.9)
    }

    print("What is your activity level ?")
    for index, key in enumerate(activity.keys(), start=1):
        print(f' {index}) {key}')
       
    
    


if __name__ == '__main__':
    main()