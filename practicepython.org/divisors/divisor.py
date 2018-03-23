def divisor(num):
    # function to search for all divisor of a number given by user
    x = list(range(1, num + 1))
    y = []
    [y.append(number) for number in x if num % number == 0]
    return y


print(divisor(int(input("Please enter a number: "))))