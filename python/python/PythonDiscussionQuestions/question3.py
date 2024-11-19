
#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 
#solution
def get_grade(score):
    """Return the grade based on the score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    elif score < 50:
        return 'Fail'
    else:
        return 'Invalid score'

def main():
    """Main function to collect scores and display grades."""
    num_students = int(input("Enter the number of students: "))
    grades = []

    for _ in range(num_students):
        score = float(input("Enter the score for student: "))
        grade = get_grade(score)
        grades.append(grade)
        print(f"The grade for the score {score} is: {grade}")

if __name__ == "__main__":
    main()
