# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.
#SOLUTION
number=int(input('Enter numbers :'))
sum= 0
sum=+number
print(f"The sum of the numbers entered is: {sum}")
while True:
    number=int(input('Enter numbers :'))
    if number == 0:
     print('STOP')
# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
#solution
# Loop through numbers 1 to 100
for num in range(1, 100):
    if num % 2 != 0:
        print(num)

