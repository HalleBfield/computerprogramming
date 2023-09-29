# A company decided to give a bonus of 5% to the employee if his/her year of service is more than 5 years. Ask the user for their salary and year of service and print the net bonus amount.

salary = int(input("What is your salary? "))
years = int(input("How long have you worked here? "))

if years >= 5:
    print(f"Your bonus will be {salary * 0.05}")
else:
    print("You do not qualify for a bonus yet.")

# Take values of the length and width of a rectangle from the user and check if it is square or not.
width= (input("what is the width of the rectangle?"))
length= (input("what is the length of the rectangle?"))
if width == length:
    print ("it is a square")
else:
    print ("it is not have a square")

# Take two int values from the user and print the greatest among them.
value1 = int(input("What is the first value? "))
value2 = int(input("what is the second value? "))

if value1 > value2:
    print(f"Value 1 is greater")
else: 
    print(f"value 2 is greater")



# Take input of age of 3 people by user and determine oldest and youngest among them.
age1 = int(input("how old is the first person?"))
age2 = int(input("how old is the second person?"))
age3 = int(input("how old is the thrid person?"))

if age1 > age2 and age1 > age3:
    print("Age 1 is the oldest")
elif age2 > age1 and age2 > age3:
    print("Age 2 is the oldest")
elif age3 > age1 and age3 > age2:
    print ("Age 3 is the oldest")

if age1 < age2 and age1 < age3:
    print ("Age 1 is the youngest")
elif age2 < age1 and age2 < age3:
    print ("Age 2 is the youngest")
elif age3 < age1 and age3 < age2:
    print ("Age 3 is the youngest")
# A student will not be allowed to sit in an exam if his/her attendance is less than 75%. Ask the user the number of classes held and the number of classes attended. Print the percentage of class attended. Is the student allowed to sit in the exam or not?

classes = int(input("how many classes are held? "))
attendance = int(input("what is your attendance? "))

if (attendance / classes) < 0.75:
    print ("you may not take the exam")
else:
    print ("you may take the exam")
