# except EOFError
# Run this and hit enter without entering any values
import sys
list1 = [1,4,6,"er",7,"**",9]
for x in list1:
    try:
        x = int(x[10])*2
        print(x)
    except Exception as e:
        print("error:", e)
    # finally:
    #     print("Finally executed")

'''
x = 5
y = 0
try:
    result = x / y
# finally:
#     print("Error")
except Exception as e:
    print("Error :",e)
    
print("integer")
'''