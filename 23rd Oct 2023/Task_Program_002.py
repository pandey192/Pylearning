#count the vowel in a string

str = input("Enter a string:")
vowels = 0
for j in str:
    if j == ("a" or "e"or"i"or"o" or"u"):
        vowels = vowels + 1
print("the number of vowels")
print(vowels)