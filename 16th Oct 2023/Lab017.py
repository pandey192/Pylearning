# problem to find MAX three

a = 10
b = 20
c = 13

max = None

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

print(max)