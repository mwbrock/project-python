# Michael Brock © June 28, 2014
# Summer Internship @ St. Petersburg College (SPC)
# Library System Simulation Program in Python - Version 1

################################################################################
# NOTE: Version 1 is one of the first Python programs that I ever wrote, and I #
# was still learning the syntax and different types of for loop constructs. It #
# does work, but it didn't quite satisfy the assignment requirements (i.e.,    #
# using nested or two-dimensional lists), so I created a Version 2 that does.  #
# I only included Version 1 here to show that there is another way to do it    #
# using multiple one-dimensional lists.                                        #
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

# Create a global two-dimensional list with 3 rows and 2 columns, where rows
# represent individual books and columns represent titles and 10-digit ISBNs.
# This list is used for testing purposes only, and the data would normally be
# obtained from a database or dictionary. I made it global so that it could be
# used by all of the functions described in the assignment.
books = [['Animal Farm', '0452284244'], ['Brave New World', '0060850523'], ['Catch-22', '0684833395']]

################################################################################
# NOTE: I tried using a nested list, as shown above, but I discovered that the #
# in operator doesn't work as expected in this case, which I confirmed online  #
# at: http://kracekumar.com/post/22512660850/python-in-operator-use-cases      #
# So I had to resolve to making separate lists of the book titles and ISBNs,   #
# with their indexes matching accordingly.                                     #
################################################################################
books_title = ['Animal Farm', 'Brave New World', 'Catch-22']
books_isbn = ['0452284244', '0060850523', '0684833395']
books_available = ['0452284244', '0060850523', '0684833395']

# The main function.
def main():
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
            lookUpISBN(title)

        elif choice == TITLE_SEARCH:
            # Get user input for book ISBN.
            isbn = input('\nEnter book ISBN: ')
            print('\nSearching for ISBN: ',isbn,'. Please wait...', sep='')

            # Call the lookUpISBN function.
            lookUpTitle(isbn)

        elif choice == QUIT_CHOICE:
            print('\nThanks for visiting the St. Petersburg Public Library! Exiting the program...')
            sys.exit()

        else:
            print('\nError: invalid selection. Please enter a valid choice.')

# The main function ends here.

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
# Then it returns the user's number. (PREDEFINED)
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
# an int in this case. (PREDEFINED)
def getCharacter():
    string = int(input('\nEnter your choice: '))
    return string

# The lookUpISBN function accepts a book title and
# returns the corresponding ISBN, or 0 if the book
# cannot be found. (PREDEFINED)
def lookUpISBN(book_title):
        
    # Create a variables to hold values.
    index = 0
    isbn = ''

    # Process the list, checking to see if user's book title is found.
    # If yes, then return ISBN. If no, then return 0 and/or a message,
    # letting the user know the book title wasn't found.
    
    # If Yes, then return book ISBN and check for availability.
    if book_title in books_title:
        # Since the index method raises a ValueError exception if the
        # item is not found in the list, a try/except statement is used.
        try:
            index = books_title.index(book_title)
            isbn = books_isbn[index]
            print('\nHooray, that book was found in our database and its ISBN is: ',isbn,'.', sep='')
        except ValueError:
            print('\nSorry, that book was not found in our database.')

        # Is the book currently available?
        print('\nChecking to see if the book is currently available. Please wait...')
		
	# Call the isBookAvailable function to check for the availability.
        isBookAvailable(isbn)
        
    # If no, then return 0 and/or a message, letting the user know
    # the book title wasn't found.
    else:
        print('\nSorry, that book was not found in our database.')
        print('\nMake sure you spelled the title correctly, including proper capitalization.')
        print('If not, choose 1 from the MENU, enter the title spelled correctly and try again.')

# The lookUpTitle function accepts a book ISBN and
# returns the corresponding Title, or none and/or
# a message value if the book cannot be found.
# (PREDEFINED)
def lookUpTitle(isbn):

    # Create variables to hold values.
    index = 0
    title = ''

    # Process the list, checking to see if user's book title is found.
    # If yes, then return ISBN and check for availability. If no, then
    # return 0 and/or a message, letting the user know the book title
	# wasn't found in the library database.
    
    # If Yes, then return book ISBN and check for availability.
    if isbn in books_isbn:
        # Since the index method raises a ValueError exception if the
        # item is not found in the list, a try/except statement is used.
        try:
            index = books_isbn.index(isbn)
            title = books_title[index]
            print('\nHooray, that book was found in our database and its title is: ',title,'.', sep='')
        except ValueError:
            print('\nSorry, that book was not found in our database.')

        # Is that the correct title?
        correct_title = input('\nIs that the correct title you are looking for? Enter \'y\' for yes or anything \nelse for no: ')

        if correct_title == 'y' or correct_title == 'Y':
            # Could've used lower() or upper() above,
            # but students haven't learned about it yet.
            
            # Is the book currently available?
            print('\nChecking to see if the book is currently available. Please wait...')
	    # Call the isBookAvailable function to check for availability.
            isBookAvailable(isbn)
        else:
            print('\nSorry, please see a librarian for help.')
        
    # If no, then return 0 and/or a message, letting the user know
    # the book title wasn't found in the library database.
    else:
        print('\nSorry, that book was not found in our database.')
        print('\nMake sure you entered the ISBN correctly.')
        print('If not, choose 2 from the MENU, enter the ISBN correctly and try again.')

# The isBookAvailable function accepts an ISBN,
# searches the library database (a list), and
# returns a "Y" or "N" indicating whether the
# book is currently available. (PREDEFINED)
def isBookAvailable(isbn):
	# If Yes, then return book ISBN.
    if isbn in books_available:
        print('\nYes, that book is currently available.')
    # If no, then return 0 and/or a message, letting the user know
    # the book title wasn't found in the library database.
    else:
        print('\nNo, that book is not currently available.')

# Call the main function to run the program.
main()
