
filename = 'listofname.txt' # select file

with open(filename,'r') as file_obj: # open file with open() function
    data = file_obj.read() # read entire content of file with read() function

print(type(data))
'''

data =[]
filename = 'listofname.txt' # select file by type file name
with open(filename) as file_obj: # open file with open() function and make alias name from filename (file_obj)
    for line in file_obj: # using for looping to read entire content line-by-line
        # data = line.split(",")
        data.append(line.strip().split('\t'))
        print(data)# we used rstrip() funtion to remove trailing spaces. it makes contents readable


filename = 'empty.txt' # select file that you want to add some text inside.
with open(filename, 'w') as file_obj: # open function with 'w' argument it is mean you will add some text in empty file
    file_obj.write("I love programming!\n") # write() function to writes some text inside files
    file_obj.write("I love Python!\n") # to write multiple lines with \n in the end of line

filename = "listofname.txt" # type file name which you want to add some text inside that
with open(filename, "a") as file_obj: # open() function with 'a' argument to appending text in file which has content
    file_obj.write("I love pandas\n") # sample instance
'''
