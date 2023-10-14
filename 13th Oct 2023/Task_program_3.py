# Use the ternary operator to find the maximum of three numbers entered by the user.

#first number
a = int(input("Enter first number"))
#second number
b = int(input("Enter second number"))
#Third number
c = int(input("Enter third number"))

max_val = a if (a>b and a>c) else b if(a<b and b>c) else c
print(max_val)