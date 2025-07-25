# reading the line of the file in a list

with open('C:/Users/maila/Selenium_Python1/readWrite.txt', 'r') as reader:
    content = reader.readlines()
    content = list(reversed(content))
    print(content)

    # writing the lines in the file
    with open('C:/Users/maila/Selenium_Python1/readWrite.txt', 'w') as writer:
        for line in content:
            writer.write(line)
