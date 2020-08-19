print("\n[STRINGS - PROBLEM 2]\n")
string = input("Enter string: ")

temp = string[0]
string = string.replace(temp, '$')
string = temp + string[1:]

print(f'\nOUTPUT >> {string}\n')
