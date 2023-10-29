# palindrom

x = input("Enter a string")

w = ""

for i in x:
    w = i + w

if (x == w):
    print("yes")
else:
    print("No")
