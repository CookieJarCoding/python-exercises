print("\n[STRINGS - PROBLEM 1]\n")

# take the two input strings from the user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# replace the last two letters of the two strings
new1 = string1[:-2] + string2[-2:]
new2 = string2[:-2] + string1[-2:]

# display the result
print('\nOUTPUT >> %s %s\n'%(new1, new2))