'''
while True:
    number = float(input("Enter a number: "))
    if number < 0:
        print("entered invalid number:", number)
        break
    print("You entered:", number)
'''


number = int(input("Enter a number: "))

count = 1

while count <= 10:
    print("Before",count)
    product = number * count
    print(product)
    count = count + 1
