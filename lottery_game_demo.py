# Copyright © June 2014 by Michael Brock 
# Summer Internship @ St. Petersburg College (SPC)
# Lottery Game Demo

# This program demonstrates a simple lottery game and is one of the first
# programming assignments that work with value-returning functions in the
# Introduction to Computer Programming class at SPC.

# Import random module - required for random number generator.
import random
# Import sys module - required for sys.exit function. (NOT in textbook!)
import sys

def main():
    # Create loop control variable.    
    play_again = "Y"

    while play_again == "Y" or play_again == "y":

        # Create accumulator (initialized to zero). MUST be inside the while
        # loop, so that it reinitializes for each new game.
        count = 0

        # Get random lottery numbers by calling the get_lottery_number
        # function and assign those values to lottery_num_n variables.
        lottery_num_1 = get_lottery_number()
        lottery_num_2 = get_lottery_number()
        lottery_num_3 = get_lottery_number()

        # Get user's guesses and assign those values to user_guess_n variables.
        user_guess_1 = int(input("Guess #1: Enter a number between 0 and 9: "))
        user_guess_2 = int(input("Guess #2: Enter a number between 0 and 9: "))
        user_guess_3 = int(input("Guess #3: Enter a number between 0 and 9: "))

        #Display the user's guesses for comparison.
        print ('Your numbers: ',user_guess_1, user_guess_2, user_guess_3)

        #Display the randomly generated lottery numbers for comparison.
        print ('Lottery numbers: ',lottery_num_1, lottery_num_2, lottery_num_3)

        # Process the results using a logic control structure.
        if user_guess_1 == lottery_num_1:
            count += 1
            print('Guess #1 matches lottery number #1.')
        elif user_guess_1 == lottery_num_2:
            count += 1
            print('Guess #1 matches lottery number #2.')
        elif user_guess_1 == lottery_num_3:
            count += 1
            print('Guess #1 matches lottery number #3.')
        else:
            print("Guess #1 did not match any of the lottery numbers.")

        if user_guess_2 == lottery_num_1:
            count += 1
            print('Guess #2 matches lottery number #1.')
        elif user_guess_2 == lottery_num_2:
            count += 1
            print('Guess #2 matches lottery number #2.')
        elif user_guess_2 == lottery_num_3:
            count += 1
            print('Guess #2 matches lottery number #3.')
        else:
            print("Guess #2 did not match any of the lottery numbers.")

        if user_guess_3 == lottery_num_1:
            count += 1
            print('Guess #3 matches lottery number #1.')
        elif user_guess_3 == lottery_num_2:
            count += 1
            print('Guess #3 matches lottery number #2.')
        elif user_guess_3 == lottery_num_3:
            count += 1
            print('Guess #3 matches lottery number #3.')
        else:
            print("Guess #3 did not match any of the lottery numbers.")

        print ("You matched",count,"lottery numbers.")

        if user_guess_1 == lottery_num_1 and user_guess_2 == lottery_num_2 and user_guess_3 == lottery_num_3:
            print ("Congratulations! You matched all 3 in order and win the max prize of $1,000,000!")
        elif count == 3:
            print ("Congratulations! You win $1000!")
        elif count == 2:
            print ("Congratulations! You win $100!")
        elif count == 1:
            print ("Congratulations! You win $10!")
        else:
            print ("Sorry, play again.")

        # Does user want to play again?
        play_again = input('Would you like to play again? Enter \"y\" or \"Y\" for yes, anything else for no: ')

    # User did not want to play again.
    print('Thanks for playing! Exiting the program...')
    sys.exit()

# The get_lottery_number function accepts no arguments and uses Python's
# built-in random.randint function to generate and return a random number
# between 0 and 9 (inclusive).
def get_lottery_number():
    random_num = random.randint(0,9)
    return random_num

# Call the main function to run the program.
main()
