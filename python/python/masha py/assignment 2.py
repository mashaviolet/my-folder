

#solution
student_name=input("Enter student's name:")
student_number=input("Enter student number:")
programming =int(input("Enter programming mark:"))
data_science=int(input("Enter data science mark:"))
computer_application=int(input("Enter computer application mark:"))
total_mark=programming + data_science + computer_application
number_units = 3
average_mark=total_mark/number_units
print(f"pThe average mark of {student_name} with {student_number} is:{average_mark:.3f}.")
#using round
average_mark=round(total_mark/number_units,3)
print("The average mark")