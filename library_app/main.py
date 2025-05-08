from library import Library
import utils


def menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n------------------ Main Menu ------------------")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. List Books by Genre")
    print("7. Inventory Summary")
    print("8. Exit")
    return input("Select an option: ").strip()


# --------------------- Start of the Program ---------------------
print("🔧 Welcome to the Library Management System! 🔧")
library = Library()  # Instancia principal de la biblioteca

while True:
    try:
        option = menu()

        match option:
            case "1":
                print("\n------------------ Add Book ------------------")
                title = utils.validate_string("Enter the book title: ")
                author = utils.validate_string("Enter the author's name: ")
                genre = utils.validate_genre(
                    "Enter the genre (fiction, non-fiction, mystery, fantasy, science, biography, children): ")
                copies = utils.validate_positive_integer("Enter the number of copies: ")
                library.add_book(title, author, genre, copies)
                print("------------------------------------------------")

            case "2":
                print("\n------------------ Search Book ------------------")
                if library.total_books == 0:
                    print("❌ No books available in the library.")
                    continue
                title = utils.validate_string("Enter the book title to search: ")
                book = library.search_book(title)
                if book:
                    print(
                        f"🔎 Found: {book['title']} by {book['author']} | Genre: {book['genre']} | Copies: {book['copies']}")
                else:
                    print(f"❌ Book '{title}' not found in the library.")
                print("------------------------------------------------")

            case "3":
                print("\n------------------ Borrow Book ------------------")
                if library.available_books == 0:
                    print("❌ No available copies in the library.")
                    continue
                title = utils.validate_string("Enter the book title to borrow: ")
                library.borrow_book(title)
                print("------------------------------------------------")

            case "4":
                print("\n------------------ Return Book ------------------")
                if library.borrowed_books == 0:
                    print("❌ No books currently borrowed.")
                    continue
                title = utils.validate_string("Enter the book title to return: ")
                library.return_book(title)
                print("------------------------------------------------")

            case "5":
                print("\n------------------ Remove Book ------------------")
                if library.total_books == 0:
                    print("❌ No books available in the library.")
                    continue
                title = utils.validate_string("Enter the book title to remove: ")
                library.remove_book(title)
                print("------------------------------------------------")

            case "6":
                print("\n------------------ List Books by Genre ------------------")
                if library.total_books == 0:
                    print("❌ No books available in the library.")
                    continue
                library.list_books_by_genre()
                print("------------------------------------------------")

            case "7":
                print("\n------------------ Inventory Summary ------------------")
                library.inventory_summary()
                print("------------------------------------------------")

            case "8":
                print("🔚 Exiting the program. Goodbye! 🔚")
                print("------------------------------------------------")
                break

            case _:
                print("❌ Invalid option. Please select a valid option from the menu.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please try again.")
