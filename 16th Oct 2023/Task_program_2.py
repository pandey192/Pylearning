# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.

x = int(input("Take a year"))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (x % 4 == 0) and (x % 100 != 0):
    print("leap year")
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (x % 100 == 0) and (x % 400 == 0):
    print("leap year")
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("not a leap year")
