import random  # to choose randomly one word from the list of words

name=input("What is your name? ") 
print("Hello ", name , ",wish you a Good Luck! \n")

words=["IITGN" , "India" , "canvas" , "apple" , "karthikram" , "python" , "Programming" , "computing" , "code" , "project"]
word= random.choice(words) # function choose one word randomly from the set of words

print("Guess the alphabets ")
guesses= ' '

chances=10

while chances>0:
    failed=0 # counts number of times the player gets failed
    
    for char in word: # takes input of  all alphabets of the word one by one

        if char in guesses: # check whether the alphabet is in the randomly choosen word
            print(char)
        else:
            print("_")

            failed+=1 # if player give incorrect alphabet then it will increase by 1
    
    if failed==0: # player win the game if there is no alphabet to be given,
                  #  means if he write all the alphabet of the randomly choosen word
        print("YOU WIN")
        print("The word is: ", word) # After player wins the game it shows the correct word
        break

    guess=input("guess a alphabet: ") # if player gave the wrong alphabet as the input 
                                       # then it will ask player to give another alphabet
    guesses+=guess
    
    if guess not in word: # checks the input alphabet given by player with the word
        chances-=1

        print("wrong") # if input doesn't match the word then 'wrong' will be given as output

        print("You have", + chances, 'more guesses') # shows how many turns are left for the player
        
        if chances==0: # if the player lost all the turns then he lost the game
            print('Sorry', name, ", You Lost")

print("\nThanks for playing, Visit again.")
                
            
