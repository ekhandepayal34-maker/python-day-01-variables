name1 = "payal"
age1 = 20
print(name1)
print(age1)
# ASSIGNING MULTIPLE VALUES

X= Y = Z= 10
print(X)
print(Y)
print(Z)
#Different value

name , age, city1 =  "payal", 20, "nashik"
print(name)
print(age)
print(city1)


#changing value
age = 20 
print(age)
age = 21
print(age)

#Veriable type
print(type(name1))
print(type(city1))
print(type(age1))

#taking input from user
name = input("Enter your name: ")

#input always string
age = input("enter age: ")
print(type(age))


#veriable deletion

name3= "riya"

del name3

# copying veriable
a= 10
b =a 
print(a)
print(b)

#swaping veriable
a = 10
b =20
a, b = b, a
print(a)
print(b)

#veriable packing
numbers = 10, 20, 30
print(numbers)


#numbers unpacking 
(a, b, c) = 10,20, 30
print(a)
print (b)
print(c)

 
 # veriable scope
name = "payal"
def show():
    print(name)
show()
 
 #local veriable

def show():
    name = "kavita"
    print(name)
show()

# global keyword
name = "payal"
def show():
    print(name)
show()

#global keyword

count = 10 
def update():
    global count
    count = 20
update()
print(count)

#constraints

PI = 3.14159
MAX_SIZE = 100


 
