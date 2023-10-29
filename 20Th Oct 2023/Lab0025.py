#Match
#Similar to switch in java
#condition is not possible in match

number = int(input("enter the number"))

match number:
    case 1:
        print("your have entered 1")
    case 2:
        print("you have entered 2")
    case _:  # underscore means no match
        print("Not matched")

