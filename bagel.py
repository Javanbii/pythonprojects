


#The Bagels game by Javan
#This is a deductive logic game where you must guess a 3-digit number based on clues


import random

num_digits = 3
max_guesses = 10


def main():
    print("""Bagels is a deductive logic game
By Javan

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
Pico            One digit is correct but in the wrong position
Fermi           One digit is correct and in the right position
Bagels          No digit is correct

For instance, if the secret number was 873 and your guess was 783, the 
clues would be Pico Fermi""" .format(num_digits))

    while True:
        #This stores the secret number the player needs to guess
        secretNum = getSecretNum()
        print("I am thinking of a number")
        print("You have {} guesses to get it" .format(max_guesses))

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ""
            #keep looping until the user enters a valid guess
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input(">")

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                 break # no need to continue
                if numGuesses > max_guesses:
                    print("You have run out of guesses. Better luck next time!")
                    print("The answer was {}" .format(secretNum))

        #Ask the player if they want to play again
        print("Do you want to play again? (Yes or No)")
        if not input(">") .lower() .startswith("y"):
            break
    print("Thanks for playing. Have a fantastic day!")


def getSecretNum():
    #returns a string made up of num_digits unique but random digits
    numbers = list("0123456789") #create a list of digits from 0 to 9
    random .shuffle(numbers) #shuffles them into any random order

    #get the first num_digits digits in the list fot the secret number:
    secretNum = ""
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    #returns a string with the pico, fermi and bagels clues

    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess [i] == secretNum[i]:
            #this means that a correct digit is in the correct place
            clues .append("Fermi")
        elif guess [i] in secretNum:
            #this means that a correct digit is in the wrong place
            clues .append("Pico")
    if len(clues) == 0:
        return "Bagels" #this means there are no correct digits at all
    else:
        #sort the clues in alphabetical order so their original order
        #does not give information away
        clues .sort()
        #make a single string from the list of string clues
        return  " " .join(clues)

def isOnlyDigits(num):
    # Returns True if num is a string made up only of digits. Otherwise returns False.
    if num == '':
        return False
    for i in num:
        if i not in '0123456789':
            return False
    return True

if __name__ == '__main__':
    main()











