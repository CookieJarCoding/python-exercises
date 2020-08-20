print("\n[STRINGS - PROBLEM 2]\n")

# take a string from the user
string = input("Enter string: ")

# save the first letter of this string
first_letter = string[0]

# replace all the succeeding repetitions of the first letter
string = string.replace(first_letter, '#')
string = first_letter + string[1:]

# display the result
print(f'\nOUTPUT >> {string}\n')
