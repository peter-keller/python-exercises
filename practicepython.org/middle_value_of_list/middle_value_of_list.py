a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def list_middle(a):
    # function to return the value of the middle element in a list
    # if the length of the list is an odd number:
    if len(a) % 2 == 1:
        return a[int(len(a) / 2 - 0.5)]
    else:
    # if the length of the list is an even number, the function takes the 2 middle elements
        return str(a[int(len(a) / 2 - 0.5)]) + "," + str(a[int(len(a) / 2 + 0.5)])


print(list_middle(a))