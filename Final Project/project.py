# [x] Get User Input - age, weight, height, activity ?
# [x] Calculate TDEE
# [] Option to loose weight
# [] Option to gain weight 
# [] Option to maintain weight


def main():
    user_data = get_user_input()

    # if user_data["goal"] == 'Loose weight':
    #     calorie_deficit(user_data)
    # elif user_data['goal'] == 'Gain weight':
    #     calorie_surplus(user_data)
    # elif user_data['goal'] == 'Maintain weight':
    #     calculate_calories(user_data)
        

    # calculate_calories(user_data)


def get_user_input():
    activities = {
        "Sedentary (little to no exercise)": float(1.2),
        "Light exercise (1-3 days per week)": float(1.375),
        "Moderate exercise (3-5 days per week)" : float(1.55),
        "Heavy exercise (6-7 days per week)" : float(1.725),
        "Very heavy exercise (Twice per day,intense)" :float(1.9)
    }

    goals = ['1) Loose weight' ,'2) Gain weight', '3) Maintain weight']

    user_data = {}
    
    try:
        age = int(input('Age: '))
        weight = int(input('Weight: '))
        height = int(input('Height: '))

        

        print('Please select your goal.')

        for goal in goals:
            print("  " + goal)
 

        user_goal = int(input("Goal: "))

        if user_goal == 1:
            goal = 'Loose weight'
        elif user_goal == 2:
            goal = 'Gain weight'
        elif user_goal == 3:
            goal = 'Maintain weight'


        print("What is your activity level ?")
    
        for index, key in enumerate(activities.keys(), start=1):
            print(f'  {index}) {key}')
        
        

        user_activity = int(input("Please select the number of the activity level: "))

        if user_activity == 1:
            activity = "Sedentary"
        elif user_activity == 2:
            activity = "Light exercise"
        elif user_activity == 3:
            activity = 'Moderate exercise'
        elif user_activity == 4:
            activity =  "Heavy exercise"
        elif user_activity == 5:
            activity = "Very heavy exercise"

        print(age, weight, height, goal, activity)
        
        
    except ValueError:
        print('Invalid input !')


def calculate_calories(input):
    age, weight, height, activity = input.values()

    base_metabolic_rate = ( 10 * weight) + ( 6.25 * height) - ( 5 * age) + 5

    total_calories = base_metabolic_rate * activity

    print(f'Your Total Daily Energy Expenditure (TDEE) is : {int(total_calories)} kcals')
    
    
def calorie_deficit():
    ...

def calorie_surplus():
    ...
    

       
    
    


if __name__ == '__main__':
    main()