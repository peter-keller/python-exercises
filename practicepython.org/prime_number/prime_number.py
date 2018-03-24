# Ask the user for a number and determine whether the number is prime or not.


def is_prime(num):
    a = [x for x in range(2, num) if num % x == 0]
    if num > 1:
        if len(a) == 0:
            return "Prime"
        else:
            return "Not prime"
    else:
        return "Not prime"


print(is_prime(int(input("Please enter a number: "))))
