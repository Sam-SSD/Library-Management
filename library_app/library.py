class Library:
    def __init__(self):
        self.books = []  # Lista para almacenar los libros
        self.genres = ["fiction", "non-fiction", "mystery", "fantasy", "science", "biography",
                       "children"]  # Lista de géneros válidos
        self.total_books = 0  # Contador de libros totales
        self.available_books = 0  # Contador de libros disponibles
        self.borrowed_books = 0  # Contador de libros prestados
        self.borrowed_books_list = []

    def add_book(self, title, author, genre, copies):
        """
        Add a new book to the library if the title is not duplicated.
        """
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"⚠️ A book with the title '{title}' already exists. Not added.")
                return
        if genre not in self.genres:
            print(f"❌ Genre '{genre}' is not valid. Book not added.")
            return
        self.books.append({"title": title, "author": author, "copies": copies, "genre": genre})
        self.total_books += 1
        self.available_books += copies
        print(f"✅ Book '{title}' added successfully.")

    def search_book(self, title):
        """
        Search for a book in the library by its title (case insensitive).
        Returns the complete book if found, or None if it doesn't exist.
        """
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        """
        Borrow a book from the library if there are available copies.
        Decreases the number of available copies by 1 but the book not exists in the library
        """
        book = self.search_book(title)
        if book:
            if book["copies"] > 0:
                book["copies"] -= 1
                self.available_books -= 1
                self.borrowed_books += 1
                self.borrowed_books_list.append(book)
                print(f"📖 Book '{title}' borrowed successfully.")
            else:
                print(f"❌ No available copies of '{title}' to borrow.")
        else:
            print(f"❌ Book '{title}' not found in the library.")


    def return_book(self, title):
        """
        Return a borrowed book to the library.
        Increases the number of available copies by 1.
        """
        for book in self.borrowed_books_list:
            if book["title"].lower() == title.lower():
                book["copies"] += 1
                self.available_books += 1
                self.borrowed_books -= 1
                self.borrowed_books_list.remove(book)
                print(f"Book '{title}' returned successfully.")
                return
        print(f"❌ Book '{title}' not found in borrowed books.")

    def remove_book(self, title):
        """
        Remove a book from the library if it has no borrowed copies.
        """
        for i, book in enumerate(self.books):
            if book["title"].lower() == title.lower():
                if book["copies"] == 0:
                    del self.books[i]
                    self.total_books -= 1
                    print(f"🗑 Book '{title}' removed successfully.")
                else:
                    print(f"❌ Cannot remove '{title}' because it has borrowed copies.")
                return
        print(f"❌ Book '{title}' not found.")

    def list_books_by_genre(self):
        """
        List all books in the library by genre.
        """
        print("\n📚 Books by Genre:")
        for genre in self.genres:
            print(f"\nGenre: {genre.capitalize()}")
            for book in self.books:
                if book["genre"].lower() == genre.lower():
                    print(f" - {book['title']} by {book['author']} | Copies: {book['copies']}")

    def inventory_summary(self):
        """
        Show a summary of the library inventory.
        Displays the total number of books and available copies.
        """
        print(f"\n📊 Inventory Summary:")
        print(f"Total books: {self.total_books}")
        print(f"Book List: {self.books}")
        print(f"Available copies: {self.available_books}")
        print(f"Borrowed books: {self.borrowed_books}")
        print(f"Borrowed books list: {self.borrowed_books_list}")
