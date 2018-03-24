# Take two lists and write a program that returns a list that contains
# only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
from random import randint

a = range(1, randint(1, 30))
b = range(1, randint(10, 40))


def list_overlap(a, b):
    overlap = [i for i in set(a) if i in b]
    return overlap


print(list_overlap(a, b))
