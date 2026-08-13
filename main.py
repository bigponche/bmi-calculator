from calculate import calculate_bmi, get_ideal_weight, get_category
    
                
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
            
#if __name__ == "__main__":