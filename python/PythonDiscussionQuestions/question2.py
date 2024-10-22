# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
#solution
def calculate_bmi():
     weight = float(input("Enter person's weight:"))
     height = float(input("Enter person's height:"))
     BMI = weight/height
     if BMI< 18.5 :
        print('Under weight')
     elif 18.5 <= BMI <= 24.9:
      print("Normal weight")
     elif 25 < BMI <=2.5:
      print("Over weight")
     else:
       print("Obese")
calculate_bmi()




# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)
#solution
def volume_of_a_cylinder():
   r=int(input("Enter the radius of the cylinder:"))
   h=int(input("Enter the height of the cylinder:"))
   import math
   pie=math.pi
   volume_of_a_cylinder=pie*r**2 * h
   print(f"The volume of the cylinder with radius {r} and height {h} is {volume_of_a_cylinder:.1f}")
volume_of_a_cylinder()