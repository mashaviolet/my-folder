#qn 7
   # write a program that converts C tem to F the program should ask the user to enter the tem in 0c and then convert to F

#solution
degrees_celsius=float(input("Enter temperature in degrees celcsius:"))
fahrenheit=float( degrees_celsius * 1.8) +32
print(f"The temperature in fahrenheit is: {fahrenheit:.1f}")


#A cars miles/gallons can be calculated with the following formula
#mpg=milesdriven/gallons of gas used
#write a progam that asks a user for the number of miles driven and gallons used it should calculate the car miles/gallon used and display the result 

#solution
miles_driven=int(input("Enter number of miles driven:"))
gallons=int(input("Enter gallons of gas used:"))
mpg=miles_driven/gallons
print(f"The car's miles driven per gallons used is:{mpg:.3f}.")
