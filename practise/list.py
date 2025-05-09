#Lists are defined by square brackets [] with elements separated by commas.
'''
"""
List syntax
 L = [item_1, item_2, ..., item_n]
"""

#Lists are mutable. They can be changed after creation.

# List with integers
a = [10, 20, 30, 40]

# Multiple data types in the same list
b = [1, True, 'Hi!', 4.3]

# List of lists
c = [['Nested', 'lists'], ['are', 'possible']]

pro_lan = ["java","c","c#","python",".net","R"]
last_lan =pro_lan[-1:]
last_lan1 = pro_lan[5:]
print(last_lan1)

pro_lan_remove = pro_lan.pop(1)
print(pro_lan_remove)
print(pro_lan)


pro_lan_replace = list(map(lambda x: "dotnet" if x == ".net" else x, pro_lan))

print(pro_lan_replace)
pro_lan.append("c")
print(len(pro_lan))
'''

gods = ['Shiva', 'Rama', 'Krishna', 'Hanumana', 'Vishnu', 'Ganesha']

# Find the length of your list
print(len(gods))

# Get the first item, the middle item and the last item of the list
print(gods[0])
print(gods[len(gods)-1])
print(gods[len(gods)//2])


