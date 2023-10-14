# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

# take first number
a= int(input("Enter first number"))

# take second number
b = int(input("Enter second number"))

max_value = a if a>b else b
print(max_value)

min_value = a if a<b else b
print(min_value)

equal_value = a if a==b else b
print(equal_value)