def guessing_game(number):
    guesses = 1
    
    while guesses <= 10:
        print("Guess number:")
        guess = input()
        guess = int(guess)
    
        if guess < number:
            print("too small")
    
    
        if guess > number:
            print("too large")
       
        guesses += 1
        
        if guess == number:
            print("this is the number!")
            break
    
    
number = 3
guesses = 1
#while guesses <= 10:
    #print("Guess number:")
    #guess = input()
    #guess = int(guess)
    
    #if guess < number:
       # print("too small")
    
    
    #if guess > number:
        #print("too large")
   
   # guesses += 1
    
    #if guess == number:
        #print("this is the number!")
        #break
        
guessing_game(1)
    
