def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# Hmm, why is just printing the sum? lets use https://pythontutor.com/visualize.html#mode-display!
# Hmm, it seems its increasing num_list and after the for loop, it prints it.
# Oh I know, I need to put the b_list append in the for loop!

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])