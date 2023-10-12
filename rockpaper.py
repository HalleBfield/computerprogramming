
user1 = input("User1:rock, Paper, Scissors?")
user2 = input("User2:rock, Paper, Scissors?")

                                                    
if user1 == "rock"or user1 =="rock":
    if user2 =="paper" or user2 =="paper":
        print("user2 wins!")
    elif user2 == "scissors" or user2 == "scissors":
        print("user1 wins!")
    elif user2 == "rock" or user2 == "rock": 
        print ("you chose the same. Try again!")

if user1 == "paper" or user1 == "paper":
    if user2 == "paper" or user2 == "paper":
        print("you chose the same. try again!")
    elif user2 == "scissors" or user2 == "scissors":
        print("user2 wins!")
    elif user2 == "rock" or user2 == "rock":
        print ("user1 wins!")

if user1 == "scissors" or user1 == "scissors":
    if user2 == "paper" or user2 == "paper":
        print ("user1 wins!")
    elif user2 == "scissors" or user2 == "scissors":
            print("you chose the same. try again!")
    elif user2 == "rock" or user2 == "rock":
            print ("user2 wins!")