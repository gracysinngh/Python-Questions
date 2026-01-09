# 1. Given an integer as input representing a student's score, print whether the student has passed or failed. (Hint: A passing score is 40 or more)


a = int (input ())
if a>= 40:
    print("Passed")  
else:
    print("Failed")


# 2.Given an integer as input representing a person's age, print whether the person is of legal age or not.
# (Hint: Legal age must be age >= 21)

a= int (input ())
if a>=21:
    print ("Legal")
else:
    print ("Not legal")

# 3.You are given two numbers. Write a program to extract the digit immediately following the decimal point in both numbers. Once done, then identify the larger among the extracted digits and display it on the screen.

num1= float (input (""))
num2= float (input (""))
a = num1*10
b = num2*10
c = int(a)
d = int(b)
ans1 = c%10
ans2 = d%10
if(ans1>ans2):
    print(ans1)
elif(ans2>ans1):
    print(ans2)
else:
    print("The numbers are equal")


# 4.Write a program that takes a single character as input and prints "True", if the character is a vowel, and "False", if the character is not a vowel. The input character can be any alphabetic character, and your solution should handle both uppercase and lowercase vowels.

alpha= str(input().lower()) 
if alpha in("a","e","i","o","u"):
    print ("True")
else:
    print ("False")

# 5.Given a number 'num' as input. You need to write a program to check if it's zero or not if it's zero print zero else print one.

num = int (input ())
if num== 0:
    print ("0")
else:
    print ("1")

# 6.Write a program to check whether a given number(!=0) is positive or negative.

# Give a number 'num' we need to check if it's a positive number or negative. If it's positive print positive and if it's negative print negative.

num= int (input ())
if num>=0:
    print ("positive")
else:
    print ("negative")

# 7.Given input as two numbers num1 and num2.Need to print the difference between the two numbers.

x,y= map (int,input ("").split())
difference = abs (x - y)
print (difference)

# 8.Given input of an year we need to print if the given year is even or odd

a= int (input ())

if a%2==0:
    print ("even")
else:
    print ("odd")

# 9.Given numbers num1 and num2, you need to write a program to print the greatest among them.

a,b = map(int, input().split())
if a==b:
    print("Both numbers are equal.")
else:
    if a>b:
        print(a)
    else:
        print(b)

# 10. Given an input year. A year is a leap year if it has 366 days. Write a program to output "leap year" if the given is a leap year otherwise print "not leap year".

a= int(input(""))
if a%4!=0:
    print("not leap year")
elif a%100==0 and a%400!=0:
    print("not leap year")
else:
    print("leap year")


# 11.You are given four integers: a, b, c, and d. Write a program to find the greatest number among these four integers.

a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))

greatest=max(a,b,c,d)

print(greatest)


# 12.Write a program to check if the given number is divisible by both 3 and 5 or not. Print "Y" if it is otherwise "N".

a=int(input(""))

if a%3==0 and a%5==0:
    print("Y")
else:
    print("N")

# 13.You are provided with the following table. Based on the student's score, you are expected to print the appropriate grade. Please write a program for the same.

# | Score Range | Grade |
# |-------------|-------|
# | 0 - 39      | F     |
# | 40 - 50     | D     |
# | 51 - 60     | C     |
# | 61 - 70     | B     |
# | 71 - 80     | A     |
# | 81 - 100    | S     |

a= int (input())

if 0<a<39:
    print ("F")

elif 40<=a<=50:
    print ("D")

elif 51<=a<60:
    print ("C")

elif 61<=a<70:
    print ("B")

elif 71<=a<80:
    print ("A")

elif 81<=a<=100:
    print ("S")

else:
    print ("Invalid input")


# 14. Write a program that takes the temperature in Celsius as input and displays a message describing the weather based on the temperature range. Use the following conditions to determine the appropriate message:

# Temp < 0: Freezing weather
# Temp 0-10: Very cold weather
# Temp 10-20: Cold weather
# Temp 20-30: Normal in temp
# Temp 30-40: It's hot
# Temp >=40: It's very hot

temperature = int(input(""))

if temperature<0:
    print("Freezing weather")
elif 0<=temperature<10:
    print("Very cold weather")
elif 10<=temperature<20:
    print("Cold weather")
elif 20<=temperature<30:
    print("Normal in temp")
elif 30<=temperature<40:
    print("It's hot")
else: 
    print("It's very hot")

# 15.Given a number n. If n is a multiple of three, print Fizz, if n is a multiple of five, print Buzz. If n is a multiple of both three and five, print FizzBuzz. Print -1 if n does not fall under any of the three constraints.

n= int(input(""))

if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print("-1")

# 16.Write a program that takes an input of a month's number and use a switch statement to output the corresponding month's name.

month = int(input())

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid")

# 17.Your task is to, write a program to print from 1 to n, where n is a given number.

n=int(input())
print_numbers=n
for i in range(1, n+1):
    print(i, end=",")

# 18.Write a program to print 1 to n in reverse order using a loop.

n=int(input())
for i in range (n, 0, -1):
    print(i, end=" ")

# 19.Write a program to print the odd number series up to N terms starting from 1.

N=int(input())
for i in range(N):
    print(2*i+1, end=" " if i<N-1 else " ")

# 20.Write a program to print all the vowels of the Input string. Given that all the Input strings are in lowercase.

n= str(input())
vowels= "aeiou"
for char in n:
    if char in vowels:
        print (char, end="")

# 21.Write a program that allows users to enter numbers unless the user enters 1 and then display the largest and smallest number respectively among all the numbers entered (including 1 as input).

max = -99999999999999
min = 9999999999999999999999999

while True:
    num = int(input())
    
   
    if num > max:
        max = num
    if num < min:
        min = num

  
    if num == 1:
        break

print(f"{max} {min}")

# 22.You are given two integers a and b.
# In one move, you can choose some integer k from 1 to 10 and add it to a or subtract it from a. In other words, you choose an integer k∈[1;10] and perform a:=a+k or a:=a−k. You may use different values of k in different moves.

# Your task is to find the minimum number of moves required to obtain b from a.

# There will be t independent test cases your program is tested against.

import math
a,b= map(int,input().split())
diff = abs(b-a)
moves= math.ceil(diff/10)
print(moves)


# 23.Given a number n, write a program to print the table of a number n. Print the multiples from 1 to 10.

n=int(input(""))
for i in range(1,11):
    print(n*i,end=" ")

# 24.Write a program to calculate the cube of all numbers from 1 to n where n is an Input number.

n=int(input(""))

for i in range(1,n+1):
	print(i*i*i, end=" ")


# 25.Given n as input. You need to write a program to find sum of 1 to n terms.

n=int(input(""))
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

# 26.Write a program to print the factors of a given number.

n=int(input(""))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=",")

# 27.You are given a weight W as input. Your task is to print all the even weights from 1 to W, following these conditions:

# If an odd weight is encountered, skip it (continue).
# If the user enters 0 or a negative weight, immediately terminate the program with the message "Process terminated."
# If the user enters 999, trigger a critical error message and stop execution (goto) and print "Error: Invalid weight detected!".


W= int(input())
if W == 999:
    print("Error: Invalid weight detected!")
elif W<=0:
    print("Process terminated.")
else:
    print("Valid even weights:", end=" ")
    for W in range(1,W+1,1):
        if W%2 != 0:
            continue
        print(W,end=" ")
    

# 28.Write a program that takes a 4-digit number as input and calculates the following:

# The sum of its digits.
# The maximum digit.
# The minimum digit.

num = input(" ")
if len(num) == 4 and num.isdigit():
    digits = [int(d) for d in num]
    digit_sum = sum(digits)
    max_digit = max(digits)
    min_digit = min(digits)
    
    print("Sum of digits:", digit_sum)
    print("Maximum digit:", max_digit)
    print("Minimum digit:", min_digit)
else:
    print("Please enter a valid 4-digit number.")


# 29.Write a program that generates a square checkerboard pattern of size n, using the characters X and O. The top-left corner of the checkerboard should always contain an X.

n = int(input())

for i in range(n):  
    for j in range(n): 
        if (i + j) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="")
    print()

