# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
def student_mark():
    mark= int(input('Enter mark scored by the student in percentage : '))
    
    if mark >=90 :
        print("Grade is A")
    elif mark >=80 :
         print("Gade is B")
    elif mark >=70 :

         print("Grade is C")
    elif mark >=60 :
         print("Grade is D")
    elif mark >=40 :
         print("Grade is E")
    else :
         print('Grade F')
student_mark()