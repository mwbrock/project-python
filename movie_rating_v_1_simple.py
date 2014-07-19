# Copyright © 2014 by Michael Brock
# Hollywood Movie Rating Program - Version 1 (Simple Solution)

# Version 1 is a simple program that demonstrates the use of loops and logic
# control structures to keep a running total in Python.

import sys # Required for sys.exit function. (NOT in textbook!)

# Global constant for the max number of tries
MAX = 3

# Define the main function
def main():

    # Create variables to hold numeric values and initialize to zero
    running_total = 0
    entries = 0
    rating =  0
    average = 0

    # Create a loop control variable for the number of tries in the input validation
    # loop and initialize it to 1 so it will start counting tries from the first entry.
    tries = 1

    # Display an introduction message to the user (OPTIONAL)
    print('This program gives a user 3 attempts to enter a valid star rating for ')
    print('the featured movie. It will display an error message and will exit the ')
    print('the program after a third failed attempt. Otherwise, it will display a ')
    print('message indicating what the user entered.\n ')

    # Get initial input from user
    rating = float(input('Enter a star rating between 0 and 4: '))

    # Validate user input
    while rating < 0 or rating > 4 and tries < MAX:
        print('ERROR: Invalid input. Please enter a number between 0 and 4. ')
        # Get input from user again
        rating = float(input('Enter a star rating between 0 and 4: '))
        tries += 1

        # Print error message and exit the program if max tries reached
        if tries >= MAX:
            print('SORRY! you have reached the maximum number of tries. Exiting the program...')
            sys.exit()

    # Print message indicating the star rating has been noted
    # if the user rating is valid and max tries not reached
    if rating >= 0 and rating <= 4 and tries < MAX:
        print('\nYou entered a star rating of',format(rating, '.2f'),'for the featured movie.')
        print('Thanks, it has been noted.')
     
# Call main function
main()
