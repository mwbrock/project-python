# Copyright © 2014 by Michael Brock
# Hollywood Movie Rating Program - Version 1
# Simple Solution.

# Version 1 is a simple program that demonstrates the use of loops and logic
# control structures to keep a running total in Python. It gives a user 3
# attempts to enter a valid star rating for the featured movie and displays
# an error message after a third failed attempt, exiting the program. Otherwise,
# it displays a message indicating what the user entered has been noted.

###########################################################################
# NOTE: This program didn't quite satisfy the assignment requirements, so #
# I wrote a Version 3 that does, which is more advanced in nature.        #
###########################################################################

import sys # Required for sys.exit function. (NOT in textbook!)

# Global constant for the max number of tries.
MAX_TRIES = 3

# Define the main function
def main():

    # Create variables to hold numeric values and initialize to zero.
    running_total = 0
    rating =  0
    average = 0

    # Display an introduction message to the user (OPTIONAL).
    print('This program gives a user 3 attempts to enter a valid star rating for ')
    print('the featured movie. It will display an error message and exit the ')
    print('program after a third failed attempt. Otherwise, it will display a ')
    print('message indicating what the user entered for the star rating was noted.\n ')

    # Get initial input from user.
    rating = float(input('Enter a star rating between 0 and 4: '))

    # Create an accumulator variable for the number of tries in the input
    # validation loop and initialize it to 1 to acount for the initial try from
    # the first entry. If you set it to 0, it will not work properly and gives
    # the user 4 tries instead of 3 as instructed.
    tries = 1

    # Validate user input
    while rating < 0 or rating > 4:
        print('ERROR: Invalid input. Please enter a number between 0 and 4. ')
        # Get input from user again.
        rating = float(input('Enter a star rating between 0 and 4: '))
        tries += 1

        # Print error message and exit the program if maximum tries reached.
        if rating < 0 or rating > 4 and tries >= MAX_TRIES:
            print("SORRY! you have reached the maximum number of tries. Exiting the program...")
            sys.exit()
        elif rating >= 0 and rating <= 4:
            print('\nYou entered a star rating of',format(rating, '.2f'),'for the featured movie.')
            print('Thanks, it has been noted.')

    # Print message indicating the star rating has been noted
    # if the user rating is valid and max tries not reached
    if rating >= 0 and rating <= 4 and tries < MAX_TRIES:
        print('\nYou entered a star rating of',format(rating, '.2f'),'for the featured movie.')
        print('Thanks, it has been noted.')
     
# Call main function to run the program.
main()
