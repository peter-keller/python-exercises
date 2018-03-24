num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Write one line of Python that takes this list num_list and makes a new list
# that has only the even elements of this list in it

def even_numbers(a):
    even_list = [i for i in a if i % 2 == 0]
    return even_list

print(even_numbers(num_list))
