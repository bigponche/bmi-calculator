from requirements import UNDERWEIGHT_LIMIT,OVERWEIGHT_LIMIT,NORMAL_LIMIT,CONVERSION

def calculate_bmi(weight, height, system):
    

    if height == 0:
        raise ZeroDivisionError('Height can not be 0')
    elif weight == 0:
            raise ValueError('Weight can not be 0')
    elif height < 0 or weight < 0:
        raise ValueError('You can not use negative numbers')   
    else:
        if system.strip().lower() == 'imperial':
            bmi = (CONVERSION * weight)/height**2
        elif system.strip().lower() == 'metric':
            bmi = weight/(height/100)**2
        else:
            raise ValueError ('Choose metric or imperial')         
    return bmi    
    
#if height.replace('.','',1).isdigit() and weight.replace('.','',1).isdigit():

def get_category(bmi):
    if bmi < UNDERWEIGHT_LIMIT:
        return 'UNDERWEIGHT'
    elif bmi < NORMAL_LIMIT:
        return 'NORMAL WEIGHT'
    elif bmi < OVERWEIGHT_LIMIT:
        return 'OVERWEIGHT'
    else: 
        return 'OBESITY'

def get_ideal_weight(height, system):
    if system.strip().lower() == 'metric':
        height_m = height / 100
        min_weight = UNDERWEIGHT_LIMIT * (height_m**2)
        max_weight = NORMAL_LIMIT * (height_m**2)
    elif system.strip().lower() == 'imperial':
        min_weight = (UNDERWEIGHT_LIMIT * (height**2)) / 703
        max_weight = (NORMAL_LIMIT * (height**2)) / 703
    else:
        raise ValueError('Choose metric or imperial')
    
    return (min_weight, max_weight)

def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero.")
            else:
                return value
        except ValueError:
            print('Enter a valid number')
            
def get_valid_system():
    
    while True:
        system = input('Enter a valid system: ')
        clean = system.lower().strip()
        if clean == 'metric':
            return clean
        elif clean == 'imperial':
            return clean
        else:
            print('That system is not valid')
            