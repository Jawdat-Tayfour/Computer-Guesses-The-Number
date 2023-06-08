import random

def c_guess(x):
    low = 1 
    high = x
    human_feedback = ''
    while human_feedback != 'c':
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low  # or high since they are equal. lol.
        human_feedback = input(f"is {guess} higher(enter H), Lower (enter L) or right(enter R) : ").lower()
        
        if human_feedback == 'l':
            low = guess + 1
        elif human_feedback == 'h':
            high = guess - 1
    
    g = input("I guessed it! Wanna play another round? Enter 'Y' for Yes or 'N' for No: ")
    if g.upper() == "N":
        print('Ok then!')
    elif g.upper() == "Y":
        c_guess(x)
    else:
        return "error"
            
i = int(input("You want me to guess a number between 1 and: "))
c_guess(i)
