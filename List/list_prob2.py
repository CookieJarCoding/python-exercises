# obtain the comma-separated value from the user
csv = input("Enter string: ")

# split the string by the coma and save it in a list
csv = csv.split(',')

# displaying each of the variables
# csv[0] is the name
# csv[1] is the age
# csv[2] is the phone number
print('\n{0:=<30}\nName: {1:30}\nAge: {2:30}\nContact: {3:30}\n{4:=<30}\n'.format('', csv[0], csv[1], csv[2], ''))