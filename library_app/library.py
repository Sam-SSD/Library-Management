class Library:
    def __init__(self):
        # Main list that stores all books as dictionaries
        self.books = []

        # Predefined list of valid genres
        self.genres = ["fiction", "non-fiction", "mystery", "fantasy", "science", "biography", "children"]

        # Tracks borrowed book titles (stored in lowercase for consistency)
        self.borrowed_books_list = []

    @property
    def total_books(self):
        """
        Returns the total number of book titles currently registered in the library.
        This counts distinct titles, not individual copies.
        """
        return len(self.books)

    @property
    def available_books(self):
        """
        Calculates the total number of available copies across all books.
        This includes all books that are not currently borrowed.
        """
        return sum(book["copies"] for book in self.books)

    @property
    def borrowed_books(self):
        """
        Calculates the total number of borrowed copies across all books.
        This is the difference between original and currently available copies.
        """
        return sum(book["original_copies"] - book["copies"] for book in self.books)

    def add_book(self, title, author, genre, copies):
        """
        Adds a new book to the library if the title is not already present
        and the genre is valid. Also saves the original number of copies
        for tracking purposes.

        Parameters:
            title (str): The title of the book.
            author (str): The author's name.
            genre (str): The book's genre.
            copies (int): Number of copies being added.
        """
        if any(book["title"].lower() == title.lower() for book in self.books):
            print(f"⚠️ A book with the title '{title}' already exists. Not added.")
            return

        if genre.lower() not in self.genres:
            print(f"❌ Genre '{genre}' is not valid. Book not added.")
            return

        self.books.append({
            "title": title,
            "author": author,
            "genre": genre.lower(),
            "copies": copies,
            "original_copies": copies
        })
        print(f"✅ Book '{title}' added successfully.")

    def search_book(self, title):
        """
        Searches for a book by its title (case-insensitive).

        Parameters:
            title (str): The title of the book to search.

        Returns:
            dict or None: The book if found, otherwise None.
        """
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        """
        Borrows a book from the library if there are available copies.
        The number of available copies is decreased and the title is logged.

        Parameters:
            title (str): The title of the book to borrow.
        """
        book = self.search_book(title)
        if not book:
            print(f"❌ Book '{title}' not found in the library.")
            return

        if book["copies"] > 0:
            book["copies"] -= 1
            self.borrowed_books_list.append(title.lower())
            print(f"📖 Book '{title}' borrowed successfully.")
        else:
            print(f"❌ No available copies of '{title}' to borrow.")

    def return_book(self, title):
        """
        Returns a previously borrowed book to the library.
        The available copies are increased by one.

        Parameters:
            title (str): The title of the book to return.
        """
        if title.lower() not in self.borrowed_books_list:
            print(f"❌ Book '{title}' not found in borrowed books.")
            return

        book = self.search_book(title)
        if book:
            book["copies"] += 1
            self.borrowed_books_list.remove(title.lower())
            print(f"📚 Book '{title}' returned successfully.")

    def remove_book(self, title):
        """
        Removes a book from the library if no active loans exist.
        Only books with all copies available can be deleted.

        Parameters:
            title (str): The title of the book to remove.
        """
        for i, book in enumerate(self.books):
            if book["title"].lower() == title.lower():
                if book["copies"] == book["original_copies"]:
                    del self.books[i]
                    print(f"🗑 Book '{title}' removed successfully.")
                else:
                    print(f"❌ Cannot remove '{title}' because it has borrowed copies.")
                return
        print(f"❌ Book '{title}' not found.")

    def list_books_by_genre(self):
        """
        Displays all books grouped by genre.
        Only genres with at least one book are shown.
        """
        print("\n📚 Books by Genre:")
        for genre in self.genres:
            genre_books = [book for book in self.books if book["genre"] == genre]
            if genre_books:
                print(f"\nGenre: {genre.capitalize()}")
                for book in genre_books:
                    print(f" - {book['title']} by {book['author']} | Copies: {book['copies']}")

    def inventory_summary(self):
        """
        Prints a summary of the library's inventory.
        Includes total titles, available copies, borrowed copies,
        and a detailed list of all books.
        """
        print(f"\n📊 Inventory Summary:")
        print(f"Total book titles: {self.total_books}")
        print(f"Total available copies: {self.available_books}")
        print(f"Total borrowed copies: {self.borrowed_books}")

        if self.books:
            print("\n📘 Book List:")
            for book in self.books:
                print(
                    f" - {book['title']} by {book['author']} | Genre: {book['genre'].capitalize()} | "
                    f"Available: {book['copies']}/{book['original_copies']}"
                )
