from library import Library
import utils

# Instantiate the main Library object
library = Library()


def handle_add_book():
    """
    Handles the logic for adding a new book to the library.
    Prompts the user for title, author, genre, and number of copies.
    """
    print("\n------------------ Add Book ------------------")
    title = utils.validate_string("Enter the book title: ")
    author = utils.validate_string("Enter the author's name: ")
    genre = utils.validate_genre(
        "Enter the genre (fiction, non-fiction, mystery, fantasy, science, biography, children): ")
    copies = utils.validate_positive_integer("Enter the number of copies: ")
    library.add_book(title, author, genre, copies)
    print("------------------------------------------------")


def handle_search_book():
    """
    Searches for a book by title and displays its information if found.
    """
    print("\n------------------ Search Book ------------------")
    if utils.validate_available_total_books(library):
        title = utils.validate_string("Enter the book title to search: ")
        book = library.search_book(title)
        if book:
            print(f"🔎 Found: {book['title']} by {book['author']} | Genre: {book['genre']} | Copies: {book['copies']}")
        else:
            print(f"❌ Book '{title}' not found in the library.")
        print("------------------------------------------------")
    else:
        return


def handle_borrow_book():
    """
    Attempts to borrow a book from the library by title.
    """
    print("\n------------------ Borrow Book ------------------")
    if utils.validate_available_books(library):
        title = utils.validate_string("Enter the book title to borrow: ")
        library.borrow_book(title)
        print("------------------------------------------------")
    else:
        return


def handle_return_book():
    """
    Attempts to return a borrowed book to the library by title.
    """
    print("\n------------------ Return Book ------------------")
    if utils.validate_borrowed_books(library):
        title = utils.validate_string("Enter the book title to return: ")
        library.return_book(title)
        print("------------------------------------------------")
    else:
        return


def handle_remove_book():
    """
    Removes a book from the library if it has no borrowed copies.
    """
    print("\n------------------ Remove Book ------------------")
    if utils.validate_available_total_books(library):
        title = utils.validate_string("Enter the book title to remove: ")
        library.remove_book(title)
        print("------------------------------------------------")
    else:
        return


def handle_list_books_by_genre():
    """
    Displays the list of books in a specific genre.
    """
    print("\n------------------ List Books by Specific Genre ------------------")
    if utils.validate_available_total_books(library):
        genre = utils.validate_genre(
            "Enter the genre (fiction, non-fiction, mystery, fantasy, science, biography, children): ")
        library.list_books_by_genre(genre)
        print("------------------------------------------------")
    else:
        return


def handle_list_books_by_all_genres():
    """
    Displays the list of books grouped by genre.
    """
    print("\n------------------ List Books by Genre ------------------")
    if utils.validate_available_total_books(library):
        library.list_books_by_all_genres()
        print("------------------------------------------------")
    else:
        return


def handle_inventory_summary():
    """
    Prints a summary of the entire library inventory.
    """
    print("\n------------------ Inventory Summary ------------------")
    library.inventory_summary()
    print("------------------------------------------------")


def menu():
    """
    Displays the main menu options and returns the user's choice.

    Returns:
        str: The selected menu option.
    """
    print("\n------------------ Main Menu ------------------")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. List Books by specific Genre")
    print("7. List Books by all Genres")
    print("8. Inventory Summary")
    print("9. Exit")
    return input("Select an option: ").strip()


# 🟢 Entry point of the program
print("🔧 Welcome to the Library Management System! 🔧")

while True:
    try:
        option = menu()

        match option:
            case "1":
                handle_add_book()
            case "2":
                handle_search_book()
            case "3":
                handle_borrow_book()
            case "4":
                handle_return_book()
            case "5":
                handle_remove_book()
            case "6":
                handle_list_books_by_genre()
            case "7":
                handle_list_books_by_all_genres()
            case "8":
                handle_inventory_summary()
            case "9":
                print("🔚 Exiting the program. Goodbye!")
                print("------------------------------------------------")
                break
            case _:
                print("❌ Invalid option. Please select a valid option from the menu.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please try again.")
