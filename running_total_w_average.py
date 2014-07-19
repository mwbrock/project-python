# Michael Brock © June 24, 2014
# Summer Internship at St. Petersburg College (SPC)
# Running Total With Average

# This program demonstrates how to keep a running total and calculates the
# average. It prompts the user for a score between 0 and 4, allowing 3 tries
# before exiting the program.

import sys # Required for sys.exit() 

# Create a global constant variable for the maximum number of tries
MAX_TRIES = 3

def main():

    # Create accumulator variables to hold values and initialize to zero.
    count = 0
    total = 0
    error = 0

    print('This program gets a series of numbers from the user and keeps a running total,')
    print('then calculates the average. You only get three tries to enter a valid number.')

    # Create a loop control variable.
    again = "y"
    
    while again == "y" or again == 'Y':
        score = int(input("\nEnter a number between 0 and 4: "))
        while score < 0 or score > 4:
            error += 1
            if error >= MAX_TRIES:
                end_program()
            print ("\nERROR: Invalid number.")
            score = int(input("\nEnter a valid number: "))
                      
        total += score
        count += 1
        again = input("\nGo again (y or n)? ")
    average = total/count
    print('\nThe average number is:',format(average,',.2f'))

def end_program():
    print("\nToo many invalid entries. Exiting program...")
    sys.exit(0)

# Call the main function to run the program.   
main()
