# Sum of Digit

n = int(input("enter a number"))


def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)
    return sum


print(getSum(n))
