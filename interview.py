# Things you can ask for can include:

# Name
# Type of programming they're interested in
# Years of experience
# Their desired salary
# Other interview-type questions
# You must include:

# A total of 10 questions
# 3 questions must require a correct answer to move on
# Variables used to save the user's information
# Professional language throughout
# A recap of the interview using formatted string literals


name = input(" What is your name? ")

ready = input(f" Hello {name} are you ready to start the interview?")
                 
Position = input(" What type of position are you interested in? ")

experience = input("How many years of experience do you have? ")

salary = input("What is your desired salary? ")

coding = input("What coding laguages do you know? ")

hours = input ("How many hours can you work?")

teamwork = input("Do you work well with others?")

solver = input("Are you a problem solver?")

traits = input("How can you contribute to the team?")
input(f"Thank you {name} for attending this interview. Let's recap what we went over.{Position},{experience},{salary}, {coding}, {hours}, {teamwork}, {solver}, {traits}, Does this sound correct? ")