 #write a program that takes two numbers as input and displays their sum difference product and quotient
#write a program that compares two integers that prints whether the first number is greater less than or equal to the second number
#write a program that checks if a given number is between 10 and 20 where by 20 is inclusive use logical operators
#write a program that prints the squares  of all integers from 1-10 using a for loop
#solution
number_one=int(input("enter first number:"))
number_two=int(input("enter second nmber:"))
#sum
sum =number_one + number_two
print(f"The sum of {number_two} and {number_one} is :{sum}")
#difference
differnce=number_two - number_one
print(f"The difference of {number_one} and {number_two} is :{differnce}")
#product
product=number_one*number_two
print(f" The product of{number_two} and {number_one} is:{product}")
#division
division=number_one/number_two
print(f"The divison of {number_one}and {number_two} is :{division}")
#modulus
modulus=number_two % number_one
print(f" The modulus of {number_one} and {number_two} is :{modulus}")
#floor divison
floor_division=number_two//number_one
print(f" The floor_divison of {number_one}and {number_two} is :{floor_division}")
#quotient
quotient=number_two/number_one
print(f" The quotient of {number_one}and {number_two} is :{quotient}")


#qn2
#comparison operators(use of if loop)
if number_one > number_two:
    print(f"{number_one} is greaterthan {number_two}")
elif number_one<number_two:
 print(f"{number_one} is lessthan {number_two}")
else:
   print(f"They are equal")

   #qn 5
   #write a program that asks a user to print her age;if the users age is greater or equal to 18 she is adult and qualified else tell her she is not qualified
   #qn 6
   #we have the following student detail and marks.enter these details from the keyboard
   #student name=Ritah Liz
   #student number=SEP23/BCS/14
   #programming=78
   #data science=89
   #computer application=55
   #CALCULATE THE AVERAGE Mark and print the answer in 3dp
   #qn 7
   # write a program that converts C tem to F the program should ask the user to enter the tem in 0c and then convert to F
   #A cars miles/gallons can be calculated with the following formula
   #mpg=milesdriven/gallons of gas used
   #write a progam that asks a user for the number of miles driven and gallons used it should calculate the car miles/gallon used and display the result 
   








