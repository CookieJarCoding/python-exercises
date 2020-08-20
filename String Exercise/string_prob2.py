print("\n[STRINGS - PROBLEM 2]\n")
string = input("Enter string: ")

first_letter = string[0]
string = string.replace(first_letter, '#')
string = first_letter + string[1:]

print(f'\nOUTPUT >> {string}\n')
