#Research What is Fibonacci series and Factorial.
#Take an input and print the series.

#The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.

#Fn = Fn-1 + Fn-2

#with seed values : F0 = 0 and F1 = 1.

#function for nth Fibonacci number

n = 10
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()






