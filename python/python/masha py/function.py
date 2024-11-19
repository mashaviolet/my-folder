#functions
#they are used to perform a paticular task
#parameters act as the data/information passed within the functions.
#area of a circle is pei*r**2.
#arguments are the values passed in the function.
#we call the function out of the function body
#create a function that returns the main components of the function

def function_components():
    print('function components are parameters arguments among others.')
function_components()    #calling function

#create a function that returns ur student name registration number and student age
def student_infor():
    student_name= 'masha violet'
    student_num='dsc/0056/ss'
    student_age=25
    print(f'{student_name} is {student_age} years old with registration number {student_num}.') 
student_infor()     #calling function 

#parameters
#create a function that returns your student name registration number and age as parameters
#take note of the variables

def student_detail(student_name,student_num,student_age):
    print(f'{student_name} is of age {student_age} and student number {student_num}.')

student_detail('sandra','dsc/0056/ss',25)    #calling a function

#return values
#approach 1
def my_name():
    name = 'masha violet'
    return name
my_name()

#approach 2
def my_name_para(name):
    name = 'masha violet'
    return name
    print(f'mame is {my_name_para()}')
#my_name_para('name')

#approach 3
def my_name_parameter(name):
    
    return name
my_name_parameter('violet masha')

#creat a function that calculates are of a triangle the base and the height must be function parameters
def area_of_a_triangle(base,height):
    area=1/2*base*height
    print(f'The area of a triangle with base {base} and height {height} is {area}')
area_of_a_triangle(8,12)  

#creat a function that calculates are of a triangle the base and the height must be function parameters enter on a keyboard
def area_of_a_triangle():
    base=int(input('Enter the base of a triangle :'))
    height=int(input('Enter the height of a triangle:'))
    area=1/2*base*height
    print(f'The area of a triangle with base {base} and height {height} is {area}')
area_of_a_triangle()  

