'''a = int(input("enter a number: "))
b = int(input ("enter a number:"))
sum = a +b
print(sum)


# program 2


H = int(input(" enter the hight of rectangle: "))
W = int (input ("enetr the width of rectangle: " ))
area_of_ractange = H * W
print(area_of_ractange) 

 # program 3 - tempreture degree change

celcius = float(input ("Enter the tempreture in celcius: "))
ferinit = (celcius * 9/5 + 32)
print(ferinit , ferinit )

 #program 4 - Swap two veriable

first_no = int(input("enter a first number: "))
second_no = int (input("enter a second no : "))

first_no, second_no = second_no, first_no
print("after_swaping")
print("first_no =",first_no)
print(" second no =",second_no)

# program 5 - SImple intrest

p = float(input("principle: "))
r = float( input("rate: "))
t = float (input ( "title" ))
si = (p * r * t ) / 100
print (" simple intrest = ", si)


# progaram 6 - shoping bill
 
item1 = float(input("Enter price of first item: "))
item2 = float(input ("enter price of second item: " ))
item3 = float(input(" enter price of third item: "))

total = item1 +item2 + item3

price = total* 0.18
bill = price + total
print("total amount =",bill)

 #program 7 - mini bank account

name = str(input (" Enter account holder name: "))
balance = float(input("enter the current amount: "))
deposite = float(input ("Enter the amount diposited: "))
withdraw = float(input("Enter the ammount which you widrawed: "))
Balance = balance + deposite - withdraw 

print("acount holder name = ",name)
print("the current balance is ", Balance)

#program 8 -  age find

day = int(input (" Ente birth day: "))
month = int(input ("Enter your birth month: "))
year = int(input (" enter your birth year: "))
current_day= int(input("Enter current day: "))
current_month =int(input("enter current month: "))
current_year = int(input ("Enter the current year:" ))
birth_days = year*365 + month*20+day
current_days = current_year *365+  current_month *30 +current_day
age_in_days = current_days - birth_days
age_in_year = age_in_days / 365
print("your age in year: ", age_in_year)
print ("your approximate age in days is: ", age_in_days)
years= age_in_days// 365
remaining_days = age_in_days/365
months = remaining_days //30
day_left = remaining_days% 30
print("years: ",years)
print("month: " , months)
print("day", day_left)


#program- 9   
correct_ans = "narendra modi"
users_ans =  input("Enter your ans: ")
if users_ans == correct_ans:
   print("correct ans ")
else:
   print(" wrong ans")'''
#program 10 - final
veriable = ("a, b, c, ")
qution = str(input("are you done your lesson :"))
nessesory_ans = "yes" 

if qution == nessesory_ans:
   print("ohk next challenge")
else:
   print("continue this lesson")




 





