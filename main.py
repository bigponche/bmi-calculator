from calculate import calculate_bmi, get_ideal_weight, get_category, get_valid_number,get_valid_system
    


def main():

    valid = get_valid_system()
    if valid == 'metric':
        height = get_valid_number('Enter your height in cm ')
        weight = get_valid_number('Enter your Weight in kgs ')
    else:
        height = get_valid_number('Enter your height in inch ')
        weight = get_valid_number('Enter your Weight in lbs ')
        
    bmi = calculate_bmi(weight,height, valid)
    category = get_category(bmi)
    min_value, max_value = get_ideal_weight(height, valid)
    print(f'Your bmi is {round(bmi,2)}')
    print(f'You are {category}')
    print(f'minimum Weight is {round(min_value,2)}')
    print(f'maximum Weight is {round(max_value,2)}')
    
if __name__ == '__main__':
    main()
            