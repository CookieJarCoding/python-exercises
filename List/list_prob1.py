my_list = ['the', 'quick', ['brown', ['fox'], 'over'], 'fence']

# concatenate and permanently change the variable by using the append method
# append the word 'jumped' next to the word 'fox'
my_list[2][1].append('jumped') 

# append the word 'the' next to the word 'over'
my_list[2].append('the')

# display the edited list
print(my_list)