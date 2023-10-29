# factorial

num = int(input("Enter a number"))
if num < 0:
    print("factorial is not possible !")
else:
    x = 1
    for i in range(1, num + 1):
        x = i * x

print(x)
