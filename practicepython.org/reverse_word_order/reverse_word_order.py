# Write a program (using functions!) that asks the user for a long
# string containing multiple words. Print back to the user the same
# string, except with the words in backwards order.
a = "My name is Peter"

def reverse(x):
     return " ".join(x.split(" ")[::-1])


print(reverse(a))
