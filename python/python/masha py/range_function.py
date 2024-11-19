# # Range function
# # range() : iterates through sequencies
# def total_marks():
#     marks = [60,70,80]
#     sum = 0
#     for mark in marks:
#         sum += mark
#     print(f"The total sum is: {sum}")
# total_marks()

# # range(start, stop, step)
# # Basic example
# # Using a loop, print all numbers from 0 to 6 
# # hint: use a range function

# for num in range(7):    # if we dont put a start num, by default its zero. To print the last num, we add a 1 to the stop
#     print(num)


# for int in range(11): # printing 0 t0 10
#     print(int)

# # example 2   
# for integer in range(1, 21):      #printing 0 t0 20
#     print(integer)
    
# Print the followinging range of even numbers (2,4,6,8,10)

def even_numbers():
    for even_num in range(2,11,2):
        print(even_num)
even_numbers()

# Print the followinging range of odd numbers (1,3,5,7,9) 

def odd_numbers():
    for odd_num in range(1,10,2):
        print(odd_num)
odd_numbers()