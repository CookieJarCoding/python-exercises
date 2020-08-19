print("\n[STRINGS - PROBLEM 1]\n")
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

new1 = string2[:2] + string1[2:]
new2 = string1[:2] + string2[2:]

print(f'\nOUTPUT >> {new1} {new2}\n')
