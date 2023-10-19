
# Have the user pick a number between 1 - 10 and a word to replace the numbers that are divisible by their number.
# Print "Prime" for all prime numbers.

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0: 
        print("Buzz")
    else:
        print(number)

bonus1 = int(input("pick a number 1-10: "))
bonus2 = input("Pick a random Word: ")

for number in range(1, 101):
    if number % bonus1 == 0:
        print(bonus2)
    else: 
        print(number)

# prime = int("2," "3," "5," 7," 11,")

# for number in range (1,102):
#     if number == prime:
#         print("Prime")