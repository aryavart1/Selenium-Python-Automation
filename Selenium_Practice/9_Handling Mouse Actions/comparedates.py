import time

d1='02/11/2021'   # DD/MM/YYYY
d2='05/12/2021'  #DD/MM/YYYY

dep_date = time.strptime(d1, "%d/%m/%Y")
return_date = time.strptime(d2, "%d/%m/%Y")

print(return_date>dep_date)  # returns true/false

# true means return date is greater than departure date
# false means return date is Not greater than departure date

