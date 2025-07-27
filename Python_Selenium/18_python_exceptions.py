ItemsInCart = 2

# To check items in cart

if ItemsInCart != 2:
    pass
    # raise Exception("Products cart count not matching")


assert (ItemsInCart == 2)

#
# try:
#     with open('C:/Users/maila/Selenium_Python1/readWrite.txt', 'r') as reader:
#         reader.read()
#
# except:
#     print("Unable to read file")



try:
    with open('C:/Users/maila/Selenium_Python1/readWrite.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning")