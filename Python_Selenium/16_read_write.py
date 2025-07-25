file = open('C:/Users/maila/Selenium_Python1/readWrite.txt')

# read n number of character by passing the parameter
# print(file.read(8))

# read one single line at a time -> readline
# print(file.readline())

line = file.readline()
while line != "":
    print(line)
    line = file.readline()

file.close()