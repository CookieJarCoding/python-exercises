print("\n[STRINGS - PROBLEM 1]\n")

string1 = raw_input("Enter first string: ")
string2 = raw_input("Enter second string: ")

new1 = string1[:-2] + string2[-2:]
new2 = string2[:-2] + string1[-2:]

print('\nOUTPUT >> %s %s\n'%(new1, new2))