# Copyright © 2014 by Michael Brock
# Hollywood Movie Rating Program - Version 1
# Simple Solution 1 with Running Total and NO Calculated Average

# Version 1 is a simple program that demonstrates the use of loops and logic
# control structures to keep a running total in Python. It gives a user three
# attempts to enter a valid star rating for the featured movie, then it either
# displays an error message after a third failed attempt, exiting the program,
# or displays a success message, indicating what the user entered has been
# noted, and exits the program.

###########################################################################
# NOTE: Versions 1 & 2 didn't quite satisfy the assignment requirements,  #
# so I wrote a Version 3 that does, which is more advanced in nature.     #
###########################################################################

import sys # Required for sys.exit function. (NOT in textbook!)

# Create a global constant for the maximum number of tries.

###########################################################################
# NOTE: In this case, I made it global simply to make it easier to change #
# later, if necessary, because it's at the top of the program.            #
###########################################################################

MAX_TRIES = 3

# Define the main function.
def main():

    # Display a descriptive introductory message to the user (OPTIONAL).
    print('This program gives a user 3 attempts to enter a valid star rating for ')
    print('the featured movie. It will display an error message and exit the ')
    print('program after a third failed attempt. Otherwise, it will display a ')
    print('message indicating what the user entered for the star rating was noted.\n ')

    # Get initial input from the user and assign it to rating variable.
    rating = float(input('Enter a star rating between 0 and 4: '))

    # Create an accumulator variable to keep a running total for the number of
    # tries in the input validation loop and initialize it to 1 to account for
    # the first try from the first entry. If you set it to 0, then it will NOT
    # work properly and gives the user four tries instead of three as assigned.
    tries = 1

    # Validate user input: While rating is out of range, display a helpful error
    # message and prompt the user to enter a valid number until maximum number
    # of tries is reached, then either exit the program immediately, or display
    # a success message and exit the program.
    while rating < 0 or rating > 4:
        # Display a helpful error message.
        print('ERROR: Invalid input. Valid numbers range between 0 and 4 (inclusive). ')
        # Get input from the user again.
        rating = float(input('Enter a star rating between 0 and 4: '))
        tries += 1
        # If maximum number of tries is reached, then display an error message
        # and exit the program.
        if rating < 0 or rating > 4 and tries >= MAX_TRIES:
            print("SORRY! you have reached the maximum number of tries. Exiting the program...")
            sys.exit(0)
        # Else if rating is within range, then display a success message...
        elif rating >= 0 and rating <= 4:
            print('\nYou entered a star rating of',format(rating, '.2f'),'for the featured movie.')
            print('Thanks for the rating, it has been noted. Exiting the program...')
            sys.exit(0)

    # If the user rating is initially valid, then display a success message and
    # exit the program.
    if rating >= 0 and rating <= 4 and tries < MAX_TRIES:
        print('\nYou entered a star rating of',format(rating, '.2f'),'for the featured movie.')
        print('Thanks for the rating, it has been noted. Exiting the program...')
        sys.exit(0)
     
# Call main function to run the program.
main()
