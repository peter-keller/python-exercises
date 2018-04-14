# Write a program (function!) that takes a list and returns a new
# list that contains all the elements of the first list minus all
# the duplicates. Extras: Write two different functions to do this
# - one using a loop and constructing a list, and another using sets.

names = ["Michele", "Robin", "Sara", "Michele"]

def list_dupl(x):
    b = []
    [b.append(i) for i in x if i not in b]
    return b


print(list_dupl(names))


def list_set(x):
    return list(set(x))


print(list_set(names))
