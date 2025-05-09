try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2025 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')