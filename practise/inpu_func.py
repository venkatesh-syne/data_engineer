
# a = input("Enter 1st number: ")
# b = input("Enter 2nd number: ")

def name_of_function1(a1,b1):
    # print(a1)
    # print(b1)
    return a1 + b1, a1*b1, a1/b1

addition = name_of_function1(int(7),int(9))
print(addition[0])

mult = name_of_function1(8,6)
print(mult[1])

mult = name_of_function1(7,6)
print(mult[1])


