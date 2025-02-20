## try...except...else...finally

def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2

def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'

def main():
    try:
        height = float(input('- enter your height (meters):'))
        weight = float(input('- enter you weight (kilograms):'))

    except ValueError as error:
        print(error)
    
    else:
        bmi = round(calculate_bmi(height, weight),1)
        evaluation = evaluate_bmi(bmi)

        print(f'your body mass index is {bmi}')
        print(f'this is considered {evaluation}')

main()## try...except...else...finally

def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2

def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'

def main():
    try:
        height = float(input('- enter your height (meters):'))
        weight = float(input('- enter you weight (kilograms):'))

    except ValueError as error:
        print(error)
    
    else:
        bmi = round(calculate_bmi(height, weight),1)
        evaluation = evaluate_bmi(bmi)

        print(f'your body mass index is {bmi}')
        print(f'this is considered {evaluation}')

main()## try...except...else...finally

def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2

def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'

def main():
    try:
        height = float(input('- enter your height (meters):'))
        weight = float(input('- enter you weight (kilograms):'))

    except ValueError as error:
        print(error)
    
    else:
        bmi = round(calculate_bmi(height, weight),1)
        evaluation = evaluate_bmi(bmi)

        print(f'your body mass index is {bmi}')
        print(f'this is considered {evaluation}')

main()
