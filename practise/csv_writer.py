
'''
import csv

# Data to be written to CSV
data = [
    ['Name', 'Department', 'Salary'],
    ['Emily Turner', 'Engineering', '65000'],
    ['Lucas Gray', 'HR', '48000'],
    ['Sophie Harris', 'Finance', '72000']
]

# Writing data to a CSV file
with open('employees1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Writing multiple rows at once
    writer.writerows(data)
'''
# li = "rt"
# print(type(li))
#
# li = ['a','b','c']
# print(type(li))
#
#
# li = ('a','b','c')
# print(type(li))
#
# li = {"a":1, "b":2}
# print(type(li))
#
# a = True
a = (5,2)
x = complex(a)
print(x)
print(type(x))