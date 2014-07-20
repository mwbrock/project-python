# Michael Brock © June 24, 2014
# Hollywood Movie Rating Program - Version 2
# Simple Solution with Calculated Average

# Version 2 is a simple program that demonstrates the use of loops and logic
# control structures to keep a running total and calculate the average in Python
# and is a little more advanced than Version 1.

###########################################################################
# NOTE: This program didn't quite satisfy the assignment requirements, so #
# I wrote a Version 3 that does, which is more advanced in nature.        #
###########################################################################

import sys # Required for sys.exit function. (NOT in textbook!)

def main():

    # Create variables to hold numeric values and initialize to zero.
    rating = 0
    average = 0

    # Create accumulators for running total and number of entries
    # and initialize to 0 (very important for accumulators).
    running_total = 0
    entries = 0

    # Create a loop control variable.
    another = 'y'

    # Display an introduction message to the user (OPTIONAL).
    print('This program accepts multiple star ratings for a featured movie, ')
    print('which are gathered from various users and averaged once all entries ')
    print('have been completed. The average is then displayed at the end.')

    # Gather a series of star ratings.
    while another == 'y' or another == 'Y':
        
        # Get input from user.
        rating = float(input('\nEnter a star rating between 0 and 4: '))
        
        # Validate user input.
        if rating < 0 or rating > 4:
            print('\nERROR: Invalid input. Valid numbers are between 0 and 4.')

        elif rating >= 0 and rating <= 4:
            running_total += rating # Same as: running_total = running_total + rating.
            entries += 1 # Same as: entries = entries + 1.
            
        another = input('\nDo you have another rating? (Enter y or Y for yes): ' )

    # Call calc_avg function and assign the value to average variable.
    # NOTE: I could've performed the calculation here without a function call.
    # For example, I could've used the following construct instead:
    # average = running_total / entries
    # However, the calc_avg function handles ZeroDivisionError exceptions, while
    # the example above doesn't and would need to be modified to do so.
    average = calc_avg(running_total, entries)

    # Display results.
    print('\nThe average star rating is',format(average, '.2f'),'out of',entries,'entries.')
    print('\nThanks for the ratings. Exiting program...')
    sys.exit(0)

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
