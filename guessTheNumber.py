import random

#selecting a random number.
number = random.randint(0,20)
#the number of chances given to the guest to gues the number.
chances = 10
count = 1
#Now loop through chances.
while chances > 0:
    #input the n'th guess.
    print("Input the " ,count, " 'th guess")
    guess = int(input())
    if guess == number:
        print("YOU WON! You have guessed the number in your ",count,"'th guess.")
        break;
    elif guess < number:
        print("You have guessed wrong the number guessed is less than the number, guess again!")
        chances-=1
        count+=1
    else:
        print("You have guessed wrong the number guessed is more than the number,guess again!")
        chances-=1
        count+=1
if not chances > 0:
    print("YOU LOSE! You have used all your guesses.")