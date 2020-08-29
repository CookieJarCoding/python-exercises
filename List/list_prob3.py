# declare the given variables
contact_list = [ 'contacts', ['family', ['mother', ['August 23, 1980', 639123456789]], ['father', ['August 22, 1980']]]]
new_number = 639987654321

# append the variable new_number to the variable contact_list.
# the main list is ['contact', []]
# the first list inside the main is ['family', [], []]
# the third list is ['mother', []] and ['father', []]
contact_list[1][2][1].append(new_number)
print(contact_list)
