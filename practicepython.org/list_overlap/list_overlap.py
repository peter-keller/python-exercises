from random import randint

a = range(1, randint(1,30))
b = range(1, randint(10,40))


def list_overlap(a, b):
    # function to list all common elements in 2 lists
    x = []
    [x.append(num) for num in a if num in b]
    return x


print(list_overlap(a, b))