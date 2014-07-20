# Copyright © 2014 by Michael Brock
# Hollywood Movie Star Rating Program - Version 3
# Advanced Solution with Calculated Average

import sys # Required for sys.exit function - NOT in textbook!

# Global constant for the maximum number of tries.
MAX_TRIES = 3

# Define the main function.
def main():

    # Create variables to hold numeric values and initialize to zero.
    running_total = 0
    entries = 0
    rating =  0
    average = 0

    # Display an introduction message to the user (OPTIONAL).
    print('This program gives a user 3 attempts per entry to enter a valid star rating for ')
    print('the featured movie. It will display an error message and exit the program after ')
    print('a third failed attempt in any given entry. Otherwise, it will continue to ask ')
    print('the user if they have another rating to enter. If yes, then it will repeat the ')
    print('validation process. Once the user has finished entering in all of the ratings, ')
    print('it will calculate the average of all the valid entries and display them below.\n ')

    # Create a loop control variable for gathering the user input.
    another = 'y'

    # Create an accumulator variable for the number of tries in the input
    # validation loop and initialize it to 1 to account for the initial try from
    # the first entry. If you set it to 0, it will not work properly and gives
    # the user 4 tries instead of 3 as instructed.
    tries = 1

    # Gather a series of star ratings.
    while another == 'y' or another == 'Y':
        
        # Get initial input from user.
        rating = float(input('Enter a star rating between 0 and 4: '))
            
        # Validate user input.
        while rating < 0 or rating > 4:
            print('ERROR: Invalid input. Please enter a number between 0 and 4. ')
            # Get input from user again.
            rating = float(input('Enter a star rating between 0 and 4: '))
            tries += 1

            # Print error message and exit the program if maximum tries reached.
            if rating < 0 or rating > 4 and tries >= MAX_TRIES:
                print("SORRY! you have reached the maximum number of tries. Exiting the program...")
                sys.exit()

        # Reinitialize the tries accumulator variable from the inner while loop to 1
        # so it will start counting over for the next set of entries gathered in the
        # outer while loop.
        tries = 1
        
        if rating >= 0 and rating <= 4 and tries < MAX_TRIES:
            running_total += rating # Same as: running_total = running_total + rating
            entries += 1 # Same as: entries = entries + 1       
            
        another = input('Do you have another rating to enter? Enter y or Y for yes: ' )

    # Call calc_avg function and assign the value to average variable.
    # NOTE: I could've performed the calculation here without a function call.
    # For example, I could've used the following construct instead:
    # average = running_total / entries
    # However, the calc_avg function handles ZeroDivisionError exceptions, while
    # the example above doesn't and would need to be modified to do so.
    average = calc_avg(running_total, entries)

    # Display the results.
    print('\nThe average star rating is',format(average, '.2f'),'out of',entries,'valid entries.')

# The calc_avg function accepts two arguments and calculates the average, which
# involves mathematical division and therefore can raise a ZeroDivisionError
# exception. Since division by zero raises an exception, it should be handled
# gracefully.
def calc_avg(total, ratings):
     # Here's one way to handle the exception (could've used try/except
     # statement instead):
    if ratings != 0:
        avg = float(total / ratings)
        return avg
    else:
        print('ERROR: Division by 0 is undefined and not allowed. Exiting the program...')
        sys.exit(0)

# Call main function to run the program.
main()
