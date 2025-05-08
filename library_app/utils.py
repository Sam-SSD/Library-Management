# utils.py

VALID_GENRES = [
    "fiction", "non-fiction", "mystery", "fantasy", "science", "biography", "children"
]


def validate_positive_integer(message):
    """
    Solicita al usuario un número entero positivo.
    """
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("❌ Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a positive integer.")


def validate_string(message):
    """
    Solicita un string no vacío y no numérico.
    """
    while True:
        value = input(message).strip()
        if not value or value.isnumeric():
            print("❌ Invalid input. Please enter a valid string.")
        else:
            return value


def validate_genre(message):
    """
    Solicita un género válido de la lista predefinida.
    """
    while True:
        value = input(message).strip().lower()
        if value not in VALID_GENRES:
            print("❌ Invalid genre. Please choose from:")
            print(f"   {', '.join(VALID_GENRES)}")
        else:
            return value
