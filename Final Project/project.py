# [x] Get User Input - age, weight, height, activity ?
# [x] Calculate TDEE
# [x] Option to loose weight
# [x] Option to gain weight 
# [x] Option to maintain weight


def main():
    user_data = get_user_input()

    if user_data["goal"] == 'Loose weight':
        calorie_deficit(user_data)
    elif user_data['goal'] == 'Gain weight':
        calorie_surplus(user_data)
    elif user_data['goal'] == 'Maintain weight':
        maintain_weight(user_data)
        



def get_user_input():
    activities = {
        "Sedentary (little to no exercise)": float(1.2),
        "Light exercise (1-3 days per week)": float(1.375),
        "Moderate exercise (3-5 days per week)" : float(1.55),
        "Heavy exercise (6-7 days per week)" : float(1.725),
        "Very heavy exercise (Twice per day,intense)" :float(1.9)
    }

    goals = ['1) Loose weight' ,'2) Gain weight', '3) Maintain weight']

    
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
            activity = activities['Sedentary (little to no exercise)']
        elif user_activity == 2:
            activity = activities['Light exercise (1-3 days per week)']
        elif user_activity == 3:
            activity = activities['Moderate exercise (3-5 days per week)']
        elif user_activity == 4:
            activity =  activities['Heavy exercise (6-7 days per week)']
        elif user_activity == 5:
            activity = activities['Very heavy exercise (Twice per day,intense)']


        return { 'age': age,
                'weight' : weight,
                'height': height,
                'goal' : goal, 
                'activity': activity }


        
        
    except ValueError:
        print('Invalid input !')


def maintain_weight(user_data):
    age, weight, height, goal, activity = user_data.values()

    base_metabolic_rate = ( 10 * weight) + ( 6.25 * height) - ( 5 * age) + 5

    total_calories = base_metabolic_rate * activity

    print(f'Your Total Daily Energy Expenditure (TDEE) is : {int(total_calories)} kcals')
    
    
def calorie_deficit(user_data):
    age, weight, height, goal, activity = user_data.values()

    base_metabolic_rate = ( 10 * weight) + ( 6.25 * height) - ( 5 * age) + 5

    total_calories = (base_metabolic_rate * activity) * 0.8

    print(f'Your daily calories in which you will loose weight are: {total_calories:.2f} kcals')


    

def calorie_surplus(user_data):
    age, weight, height, goal, activity = user_data.values()

    base_metabolic_rate = ( 10 * weight) + ( 6.25 * height) - ( 5 * age) + 5

    total_calories = (base_metabolic_rate * activity) * 1.2

    print(f'Your daily calories in which you will gain weight are: {total_calories:.2f} kcals')
    
    

       
    
    


if __name__ == '__main__':
    main()