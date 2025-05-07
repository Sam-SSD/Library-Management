def validate_positive_integer(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("❌ Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a positive integer.")
            message = input("Enter the number of copies: ")


def validate_string(message):
    while True:
        try:
            value = input(message).strip()
            if not value or value.isnumeric():
                print("❌ Invalid input. Please enter a valid string.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid string.")
            message = input("Enter the book title: ")


def validate_genre(message):
    genres = ["fiction", "non-fiction", "mystery", "fantasy", "science", "biography", "children"]
    while True:
        try:
            value = input(message).strip().lower()
            if value not in genres:
                print("❌ Invalid genre. Please choose from: (fiction, non-fiction, mystery, fantasy, science, biography, children).")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid genre.")