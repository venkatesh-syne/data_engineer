# s1 = {'HE170B', 'HE210B', 'HE190A', 'HE200A', 'HE210A', 'HE210A'}
# s2 = {'HE200A', 'HE210A', 'HE240A', 'HE200A', 'HE210B', 'HE340A'}
# s_intersection = s1.intersection(s2)
# s_union = s1.union(s2)
# print(s_intersection)
# print(s_union)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }


# for persons in person:
#     if "address" in persons:
#         print(person["address"]["street"])

# for key in person:
#     print(key)

for key, value in person.items():
    print(key, ":", value)

# if "address" in person:
#     if "street1" in person["address"]:
#         print(person["address"]["street"])
#     elif "street3" in person["address"]:
#         print(person["address"]["street"])
#     else:
#         print("not found")
#
# else:
#     print("not found")



