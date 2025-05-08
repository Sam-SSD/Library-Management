# Predefined list of accepted genres
VALID_GENRES = [
    "fiction", "non-fiction", "mystery", "fantasy", "science", "biography", "children"
]


def validate_positive_integer(message: str) -> int:
    """
    Prompts the user to enter a positive integer.
    Keeps asking until valid input is provided.

    Args:
        message (str): Prompt message to display.

    Returns:
        int: A valid positive integer.
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


def validate_string(message: str) -> str:
    """
    Prompts the user to enter a non-empty, non-numeric string.
    Useful for names, titles, etc.

    Args:
        message (str): Prompt message to display.

    Returns:
        str: A valid string.
    """
    while True:
        value = input(message).strip()
        if not value or value.isnumeric():
            print("❌ Invalid input. Please enter a valid string.")
        else:
            return value


def validate_genre(message: str) -> str:
    """
    Prompts the user to enter a valid genre.
    Keeps asking until the input matches one of the predefined genres.

    Args:
        message (str): Prompt message to display.

    Returns:
        str: A valid genre string in lowercase.
    """
    while True:
        value = input(message).strip().lower()
        if value not in VALID_GENRES:
            print("❌ Invalid genre. Please choose from:")
            print(f"   {', '.join(VALID_GENRES)}")
        else:
            return value
