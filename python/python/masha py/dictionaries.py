# Dictinaries: stores data in a key value pair
# syntax; the keys are on the left and values on right
# keys can never be lists, tuples or sets
student ={"name": "Gillian", 
          "age": 22, 
          "location": "Muyenga"
          }
print(student)

fruits = {1:"Apple",
          2: "Orange",
          3:"Banana"
          }
print(fruits)

# Accesing items
# we use keys to access a value

print(student["name"]) 
print(student["age"])
print(student["location"])


# print the keys of the stundent dictionarys
print(student.keys())

# print the length of the dictionaries
print(len(student))

# Adding items
# add a key contact to the student dict
student["contact"] = "07094383745"
print(student)

# Changing items
# update the student name Gillian to Apio Gillian
student["name"] = "Apio Gillian"
print(student)

# print all values of the dictionary
print(student.values())

# Removing items
# Remove the contact key from the dictionary
student.pop("contact")
print(student)