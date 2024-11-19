#data collection deals with multiple data
#lists store items
#syntax = var_name=[]
student_name =['masha','violah','brendah','violet','cathy','agie'] #string
student_mark =[56,45,76,86,49,65] #integer

#access the the whole list
print(student_name , type(student_name))

#accessing list items
print(student_name[0])   #first item
print(student_name[1])   #second item
print(student_name[2])   #third item
print(student_name[3])   #fourth item
print(student_name[4])   #fifth item
print(student_name[5])   #sixth item

#appending -adding new items in the list
#at the end
student_name.append('michelle')
print(student_name)

#at a particular position
student_name.insert(2,'faith')
print(student_name)

