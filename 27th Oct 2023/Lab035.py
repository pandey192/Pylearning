#Scoping of data

num = 20
def multiple_by_10(n):
    n *= 10
    num = n
    print("value of num inside function:",num)
    return n
op = multiple_by_10(num)
print(op)
print("value of num outside function",num)