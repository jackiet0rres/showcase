import book_db_access
import checkout_db_access
from Book import Book
from Checkout import Checkout
from db_connect import DBConnect


def get_command():
    print("Here are the options")
    print("1 Display a book by ISBN")
    print("2 Get books by category")
    print("3 Check out a book")
    print("4 Return a book")
    print("5 Return the number of books checked out by a patron")
    print("6 Search books starting with a letter")
    print("7 List books with a page count higher than a specified value")
    print("Q Quit the system")
    com = input()
    return com

def do_display_by_isbn():
    print("Enter the ISBN")
    isbn = input()
    book = book_db_access.retrieve_by_isbn(isbn)
    if book == None:
        print("This book is not in our library")
    else:
        book.display()

def display_books_in_category():
    print("Listing books in a category")
    print("Here are the categories you can choose from ")
    categories = book_db_access.list_categories()

    for cat in categories:
        print(cat, end=" | ")
    print()
    print("Choose a category")
    category = input()

    catlist = book_db_access.retrieve_books_by_category(category)
    if catlist:
        for cat in catlist:
            cat.display()
    else:
        print("There are no books matching that category")

def do_checkout():
    print("Enter the patron infomation")
    print("Patron ID:")
    patronid = input()
    print("First name:")
    fname = input()
    print("Last name:")
    lname = input()
    print("ISBN of the book being checked out:")
    isbn=input()
    book = book_db_access.retrieve_by_isbn(isbn)
    if book==None:
        print("This book does not exist in the library")
    else:
        print("You are checking out ",book.title)
        checkout = Checkout(patronid,isbn, fname, lname, "checked out")
        id = checkout_db_access.insert_checkout(checkout)
        print("id is ", id)


def return_book():
    print("Enter the patron id")
    pid = input()
    print("Enter the ISBN of the book to be returned")
    isbn=input()
    numUpdate = checkout_db_access.return_book(pid,isbn)
    if numUpdate==0:
        print("The book is not listed as checked out by the patron")
    else:
        print("The book was returned")


def get_num_checkout_rec_by_patron():
    print("will display the number of checkouts/returns for a patron")
    print("Enter the patron id")
    pid = input()
    print("Enter status ")
    status = input()
    num_records = checkout_db_access.num_records(pid, status)
    print("Patron has ", num_records, " books ", status)

def search_books_by_letter():
    print("Enter the starting letter:")
    letter = input().strip()
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabetical character.")
        return

    books = book_db_access.retrieve_books_by_letter(letter)
    if books:
        for book in books:
            book.display()
    else:
        print("No books found starting with the letter", letter)

def search_books_by_page_count():
    print("Enter the minimum page count:")
    try:
        min_page_count = int(input().strip())  ##makes sure input is an integer
        books = book_db_access.retrieve_books_by_page_count(min_page_count)
        if books:
            for book in books:
                book.display()
        else:
            print(f"No books found with a page count higher than {min_page_count}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


print("Welcome to the Library Database")

cmd = get_command()

while cmd != 'Q':
    if cmd == '1':
        book  = do_display_by_isbn()

    if cmd == '2':
        display_books_in_category()

    if cmd == '3':
        do_checkout()

    if cmd == '4':
        return_book()

    if cmd =='5':
        get_num_checkout_rec_by_patron()

    if cmd == '6':
        search_books_by_letter()

    if cmd == '7':
        search_books_by_page_count()

    cmd = get_command()
print("bye")
