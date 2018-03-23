a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def less_than_ten(a):
    # function to return new list that contains numbers less or equal than 5
    x = []
    [x.append(i) for i in a if i <= 5]
    return x


print(less_than_ten(a))
