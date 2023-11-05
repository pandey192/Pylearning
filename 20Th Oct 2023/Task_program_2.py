# palindrom

x = input("Enter a string")

w = ""

for i in x:
    w = i + w

if (x == w):
    print("yes")
else:
    print("No")



#By lamda function

reverse_str = lambda orignal_str:orignal_str[::-1]

if reverse_str("pramod")=="pramod":
    print("its palindrom")
else:
    print("not a plindorm")
