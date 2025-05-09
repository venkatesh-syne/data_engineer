def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return fact

my_number = int(input('please enter a positive integer: '))
print('the factorial of your integer is:', factorial(my_number))


# def factorial(number):
#
#     fact = 1
#     if number > 1:
#         fact = number*(factorial(number-1))
#     return fact

# my_number = int(input('please enter a positive integer: '))
# print('the factorial of your integer is:', factorial(my_number,'2'))