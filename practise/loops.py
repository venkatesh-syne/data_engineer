#for loop:
# numbers = (0,1,2,3,4,5,6)
# for number in numbers:
#     # print(number)
#     if number == 6:
#         continue
#     print('Next number should be ', number + 1) if number != 6 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

'''
count = 1
while count < 3:
    print(count)
    count = count + 1
else:
    print(count)


if count < 3:
    count = count + 1
    print(count)
else:
    print("count is lesser",count)
'''

# val = int(input("Enter the Value : "))
sum1 = 9
for i in range(0,6):
    sum1 +=i
    print(f'{sum1} + {i} =',sum1)


'''
0 + 0 = 0
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
'''



'''
0 * $
1 * $ = $ 
2 * $ = $$
3 * $ = $$$
'''

# txt = "I love apples, apple are my favorite fruit"
#
# x = txt.count("apple")
#
# print(x)