file = open('C:/Users/maila/Selenium_Python1/readWrite.txt')

# read n number of character by passing the parameter
# print(file.read(8))

# read one single line at a time -> readline
# print(file.readline())

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()
#
# file.close()


# readLines -> creates a list where each line is stored as a element in the list
# print(file.readlines())

for line in file.readlines():
    print(line)


