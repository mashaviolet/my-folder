#solution 3
x=int(input("Enter number:"))
print(x>10 and x<=20)
print(x>10 or x<=20)
print(not(x>10 and x<=20))

#solution 4
integers = [1,2,3,4,5,6,7,8,9,10]
for y in integers: 
 print(y*y)

 #solution 5
 age=int(input("enter age:"))
 if age >= 18:
  print(f"{age}, she is an adult and qualified.")
 elif age < 18:
  print(f"{age},she is not an adult and not qualified.")
 else:
  print(",she is not an adult and not qualified.")

 