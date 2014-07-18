# Michael Brock © June 28, 2014
# Summer Internship @ St. Petersburg College (SPC)
# Library System Simulation Program in Python - Version 2

################################################################################
# NOTE: Version 2 was made to satisfy the assignment requirements of using a   #
# "list of lists" (a.k.a. "nested list" or "two-dimensional list"). Also, I    #
# cleaned up the code and used different logic control structures herein.        #
################################################################################

# This program simulates a library system with library card number validation,
# a search options menu, and various functions to test, manipulate and retrieve
# data. The search options menu allows users to search for a book by ISBN or by
# title, or to quit the program. The exercise has predefined function signatures
# that the students are required to implement and use in their code whenever
# they are appropriate.

import sys # Required for sys.exit() function. (NOT in textbook!)

# Create global constants for the menu choices.
ISBN_SEARCH = 1
TITLE_SEARCH = 2
QUIT_CHOICE = 3
    
################################################################################
# NOTE: Normally, this type of program would be accessing the data from either #
# databases or dictionaries. But since the students working on this exercise   #
# have not been introduced to these concepts yet and are working with lists, I #
# wrote this program with that in mind.                                        #
################################################################################

# Create a global two-dimensional list with 3 rows and 3 columns, where rows
# represent individual books and columns represent titles, 10-digit ISBNs and
# a 'y' or 'n' character for availability. This list is used for testing purposes
# only, and the data would normally be obtained from a database or dictionary. I
# made it global so that it could be used by all of the functions described in
# the assignment.
books = [
    ['Animal Farm', '0452284244', 'N'],
    ['Brave New World', '0060850523', 'Y'],
    ['Catch-22', '0684833395', 'Y']
    ]

# Create global constants for ROWS and COLS to be used in functions.
ROWS = len(books)
COLS = len(books)

# The main function.
def main():

    # Create a variables to hold values.
    isbn = 0
    title = ''
    
    # Call the getNumber function to get the library card number from user 
    # and assign it to the library_card_number variable.
    library_card_number = getNumber()

    # Display library_card_number to make sure we have the correct number.
    print('\nYou entered library card number:',library_card_number)
    print('That is a valid library card number.\nWelcome! You may proceed...')

    # The choice variable controls the while loop and holds the user's choice.
    choice = 0

    # While users don't choose to quit, display menu with search and quit choices.
    while choice != QUIT_CHOICE:
        
        # Display the menu.
        display_menu()

        # Call the getCharacter function to get the user's choice.
        choice = getCharacter()

        # Create a logic control structure to handle user choices
        # and to perform the selected action.
        if choice == ISBN_SEARCH:
            
            # Get user input for book title.
            title = input('\nEnter book title: ')
            print('\nSearching for ',title,'. Please wait...', sep='')

            # Call the lookUpISBN function.
            isbn = lookUpISBN(title)

            if isbn != 0:
                print('\nHooray, that book was found in our database and its ISBN is: ',isbn,'.', sep='')

                # Is the book currently available?
                print('\nChecking to see if the book is currently available. Please wait...')

                # Call the isBookAvailable function to check for the availability.
                isBookAvailable(isbn)

            else:
                print('\nSorry, that book was not found in our database.')
                print('\nMake sure you spelled the title correctly, including proper capitalization.')
                print('If not, choose 1 from the MENU, enter the title spelled correctly and try again.')

        elif choice == TITLE_SEARCH:
            
            # Get user input for book ISBN.
            isbn = input('\nEnter book ISBN: ')
            print('\nSearching for ISBN: ',isbn,'. Please wait...', sep='')

            # Call the lookUpISBN function.
            title = lookUpTitle(isbn)

            if title != 0:
                print('\nHooray, that book was found in our database and its title is: ',title,'.', sep='')

                # Is that the correct title?
                correct_title = input('\nIs that the correct title you are looking for? Enter \"y\" or \"Y\" for yes, or \nanything else for no: ')

                if correct_title == 'y' or correct_title == 'Y':
                    # Could've used lower() or upper() above,
                    # but students haven't learned about it yet.

                    # Is the book currently available?
                    print('\nChecking to see if the book is currently available. Please wait...')

                    # Call the isBookAvailable function to check for availability.
                    isBookAvailable(isbn)

                else:
                    print('\nSorry, please see a librarian for help.')

            # If no, then return a message, letting the user know
            # the book title wasn't found in the library database.
            else:
                print('\nSorry, that book was not found in our database.')
                print('\nMake sure you entered the ISBN correctly.')
                print('If not, choose 2 from the MENU, enter the ISBN correctly and try again.')

        elif choice == QUIT_CHOICE:
            print('\nThanks for visiting the St. Petersburg Public Library! Exiting the program...')
            sys.exit()

        else:
            print('\nError: invalid selection. Please enter a valid choice.')

# End of main function.

# The display_menu function displays a menu that
# allows users to search for a book by ISBN or
# by title, or to quit the program.
def display_menu():
	print('\n\tMENU')
	print('1) Search for book by Title')
	print('2) Search for book by ISBN')
	print('3) Quit')

# The getNumber function prompts the user to enter
# their library card number and checks to make sure
# it's within the range of the high and low numbers.
# Then it returns the user's number.
# (PREDEFINED FUNCTION SIGNATURE)
def getNumber():
    
    # Get the user's library card number and validate
    # to make sure it's in the correct range.
    card_number = int(input('Enter your library card number: '))

    # Validate user's library card number.
    while card_number < 1000 or card_number > 9999:
        print('\nERROR: Invalid library card number!..')
        print('Valid card numbers are from 1000 to 9999.')
        card_number = int(input('\nEnter a valid library card number: '))

    return card_number

# The getCharacter function prompts the user for a
# character string and returns the string, casted as
# an int in this case. (PREDEFINED FUNCTION SIGNATURE)
def getCharacter():
    string = int(input('\nEnter your choice: '))
    return string

# The lookUpISBN function accepts a book title and
# returns the corresponding ISBN, or 0 if the book
# cannot be found. (PREDEFINED FUNCTION SIGNATURE)
def lookUpISBN(title):
        
    # Create a variables to hold values.
    isbn = 0

    # Process the list, checking to see if user's book title is found.
    # If yes, then return ISBN. If no, then return 0.	
    for r in range(ROWS):
        for c in range(COLS):
            # If Yes, then return book ISBN.
            if title == books[r][c]:
                isbn = books[r][1]
                return isbn
    # If no, then return 0.
    return 0

# The lookUpTitle function accepts a book ISBN and
# returns the corresponding title, or 0 if the
# book cannot be found. (PREDEFINED FUNCTION SIGNATURE)
def lookUpTitle(isbn):

    # Create variables to hold values.
    title = ''

    # Process the list, checking to see if user's book title is found.
    # If yes, then return book title. If no, then return 0.    
    for r in range(ROWS):
        for c in range(COLS):
            # If Yes, then return book title.
            if isbn == books[r][1]:
                title = books[r][0]
                return title
    # If no, then return 0.
    return 0

# The isBookAvailable function accepts an ISBN,
# searches the library database (a list), and
# returns a "Y" or "N" indicating whether the
# book is currently available.
# (PREDEFINED FUNCTION SIGNATURE)
def isBookAvailable(isbn):
    
    # Create variables to hold values.
    available = ''

    # Process the list, checking to see if user's book is available.
    # If yes, then return 'Y' and a message indicating that it is 
    # currently available. If no, then return 'N' and/or a message
    # indicating that it is not currently available.
    for r in range(ROWS):
        for c in range(COLS):
            # If the ISBN is found, then check for availability.
            if isbn == books[r][1]:
                available = books[r][2]

    # If yes, then return 'Y' and/or a message indicating that
    # it is currently available.
    if available.upper() == 'Y':
        print('\nYes, that book is currently available.')
    # If no, then return 'N' and/or a message indicating that
    # it is not currently available.
    else:
        print('\nNo, that book is not currently available.')

# Call the main function to run the program.
main()
