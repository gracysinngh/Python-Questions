#1. Write a program to check whether the input string's first letter is a vowel or not.

a=input()
if a[0].lower() in ['a','e','i','o','u']:
    print("Yes")
else:
    print("No")