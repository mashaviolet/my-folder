# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
#solution

x1=int(input('Enter the x1 value :'))
x2=int(input('Enter the x2 value :'))
y1=int(input('Enter the x2 value :'))
y2=int(input('Enter the x2 value :'))
import math

distance = math.sqrt ((x2-x1)**2 +(y2 - y1)**2)
print(f'The distance between two codinate points is {distance}')
# Question 1(ii)
# Write a Python program to find maximum between three numbers.
number1=int(input('Enter first number :'))
number2=int(input('Enter second number :'))
number3=int(input('Enter third number :'))
import math
maximum_value=max(number1,number2,number3)
print(maximum_value)