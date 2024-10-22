# operator precedence
#describes the order through which operations are performed in an expression
#operators with higher precedence are always executed  first.
#examples

result = 3*4+5
print(result)

result_two=3*(4+5)
print(result_two)

result_three=3*4+5-1
print(result_three)

result_four = 3*(4+5)-1
print(result_four)

#General operator precedence
#what will be the output of the following expression

result_five = 5*3**2
print(result_five)

mean=(5+3)*2**2-10/2
print(mean)

result_seven =25/5+2*1
print(result_seven)

result_eight = (25/5) + 2 *1
print(result_eight)

#control flow structures
#These determine the order in which a program can be executed basing on condditons or loops

#types
#conditional statements 
#execute the program based on a particular condition eg if elif else
#create a program that asks a user to for the food type bought from the market the progrem should print you bought
#chicken if the user enters chicken or print liver if the user enters liver else if not the two print u bought fish

food_type = input("Enter food type bought :\n")

if food_type=="chicken":
    print(f"You have bought chicken from the market.")
elif food_type=='liver':
    print(f"You have bought liver from the market.")
else:
    print(f"You have bought fish from the market.")

#comment

food_type = input("Enter food type bought :\n")
if food_type!='chicken' or food_type!='liver'   or food_type!= 'fish':
 print('please choose from chicken, liver or fish')
if food_type=="chicken":
    print(f"You have bought chicken from the market.")
elif food_type=='liver':
    print(f"You have bought liver from the market.")
elif food_type == 'fish':
    print('You have bought fish')   
else:
    print(f"Incorrect syntax.")