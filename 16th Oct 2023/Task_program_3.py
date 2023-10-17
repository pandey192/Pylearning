#Write a program that classifies a triangle based on its side lengths.

#Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).


side1 = float(input("first side of triangle"))
side2 = float(input("second side of triangle"))
side3 = float(input("third side of triangle"))

if side1 == side2 == side3:
    print("triangle is equilateral")
elif(side1 == side2 != side3) or (side1 != side2 == side3) or(side1 == side3 != side2) :
    print("triangle is isosceles")
else:
    print("triangle is scalene")