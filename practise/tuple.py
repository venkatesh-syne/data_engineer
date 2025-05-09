# tpl = ('item1', 'item2', 'item3')
# print(tpl)
#
# lst = ['item1', 'item2', 'item3', 'item4', 'item1']
# print(lst)
# st = set(lst)
# print(st)
my_new_dict = {'name': ["darshil", 'jac', 'rahul'], "surname": ["parmar",'asd','asdas'], "age": [25,26,27]}
print(my_new_dict)
val = my_new_dict['age']
print(val)
if 25 in val:
    print(val)
    print(val.count(25))
else:
    print("not found")