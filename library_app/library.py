class Library:
    def __init__(self):
        # Lista principal para almacenar los libros como diccionarios
        self.books = []

        # Lista válida de géneros predefinidos
        self.genres = ["fiction", "non-fiction", "mystery", "fantasy", "science", "biography", "children"]

        # Lista de títulos (en minúsculas) actualmente prestados
        self.borrowed_books_list = []

    @property
    def total_books(self):
        """Cantidad de títulos registrados"""
        return len(self.books)

    @property
    def available_books(self):
        """Suma total de copias disponibles en todos los libros"""
        return sum(book["copies"] for book in self.books)

    @property
    def borrowed_books(self):
        """Suma de copias prestadas en todos los libros"""
        return sum(book["original_copies"] - book["copies"] for book in self.books)

    def add_book(self, title, author, genre, copies):
        """
        Agrega un nuevo libro a la biblioteca, si el título no está repetido y el género es válido.
        Guarda las copias originales para poder calcular préstamos.
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
        Busca un libro por su título (no sensible a mayúsculas).
        """
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        """
        Presta una copia del libro si está disponible.
        """
        book = self.search_book(title)
        if not book:
            print(f"❌ Book '{title}' not found in the library.")
            return

        if book["copies"] > 0:
            book["copies"] -= 1
            self.borrowed_books_list.append(title.lower())  # solo guardamos el título
            print(f"📖 Book '{title}' borrowed successfully.")
        else:
            print(f"❌ No available copies of '{title}' to borrow.")

    def return_book(self, title):
        """
        Devuelve una copia del libro prestado.
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
        Elimina un libro si no tiene préstamos activos (todas sus copias están disponibles).
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
        Muestra todos los libros agrupados por género.
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
        Muestra un resumen del inventario de la biblioteca.
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
