#Create a program
#Take 5 numbers from the user
#Add 1 -2 duplicate
#print non duplicate numbers

N1 = int(input("take a first number"))
N2 = int(input("take a second number"))
N3 = int(input("take a third number"))
N4 = int(input("take a fourth number"))
N5 = int(input("take a fifth number"))

list = [N1,N2,N3,N4,N5]
New_List = set(list)
print(New_List)