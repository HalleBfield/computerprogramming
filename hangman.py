word = 'donkey'

print("Welcome to hangman!")
   
guesses1 = ''  
turns1 = 5
   
while turns1 > 0:  
    failed1 = 0  
        
    for char in word:  
           
        if char in guesses1:  
            print(char)  
               
        else:  
            print("_")  
            failed1 += 1  
               
    if failed1 == 0:  
        print("You guessed correct, good job!")  
           
        print("The correct word is:,donkey")  
        break  
    
    guess1 = input("Guess a letter:")  
    guesses1 += guess1     
    if guess1 not in word:      
        turns1 -= 1   
           
        print("incorrect")  

        print("You have ", + turns1, 'more guesses ')  
           
        if turns1 == 0:  
            print("you lose, the word is donkey")  

