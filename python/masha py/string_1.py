#strings in depth

marks=[90,60,70]
name ="cathy"
print(name[0])
print(name[4])
#looping through strings
for character in name:
    print(name[4])
address = "kamokya"
for place in address:
    print(address[6])
    print(place)
#slicing in strings
#this is the accessing a ranga of characters 
#example
name="cathy"
print(name[1:3])
print(name[0:4])
print(name[1:5])
print(name[0:2])
#to get a given character add (+1) to it
#exmple 2
name="cathy"
print(name[_:4])
#answer is cath
message="Hello"
print(message[0:3])
print(message[-1])
#answer is o
print(message[-1:-5])
print(message[-5:-3])
print(message[-4:_])
print(message[4:_])
#f string
name="cathy"
age=21
print(f"my name is{name} and am {age} years old")
weight=58.41318
print(f"my name is {name}and am {age} years old i weigh{weight:.2f}")
total_cost=300000
print(f"a new car is{total_cost:,}")
name="cathy"
total_length=len(name)
address="fromkamokya"
print(len(name))
print(len(address))
name="CATHY"
print(len(name))
print(len(name.upper))
name="cathy\n masha\n"
print(name)

