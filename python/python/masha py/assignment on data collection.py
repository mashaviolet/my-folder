#assignment
#given  a sample list,
#student_name=[patricia, anitah ,faith,phiona] 
#and student_mark=[80,56,78,90]
#print patricia, anitah ,faith,phiona
#  add masha at the fourth position
#update the name phionah to phionah aladina
#display the length of the student list 
#print all the students name using a for loop
#calculate the total marks for the students mark variable the anwer is 304

#SOLUTION

student_name =['PATRICIA','ANITAH','FAITH','PHIONA'] #string
print(student_name)   

student_name.insert(3,'MASHA')  #adding masha
print(student_name)   

print(len(student_name))  #length

student_name[4]='PHIONA ALADINA' #updating phiona to phiona aladina
print(student_name)

for name in student_name: #for loop
    print(name)

student_mark=[80,56,78,90]
total_mark= sum(student_mark)
print(total_mark)