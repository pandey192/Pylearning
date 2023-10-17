# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#input- score - 89
#output- B

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

x = int(input("Take a number form user"))

if x in range(90,100):
    print("A")
elif x in range(80,89):
    print("B")
elif x in range(70,79):
    print("C")
elif x in range(60-69):
    print("D")
else:
    print("F")
