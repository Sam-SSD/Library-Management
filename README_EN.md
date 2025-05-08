![Library management system banner](https://github.com/user-attachments/assets/b71cf61c-3eb0-41a1-820e-e84f4ca650fd)

# 📚 Library Management System

### 📘 Versión en español  
[Haz clic aquí para ver el README en español](./README.md)

---

## 📌 Project Description

This project is designed to simulate a **library management system** where users can add, borrow, return, and manage books through an interactive console interface. The system is built using **Python**, with a clean architecture based on **object-oriented programming** and **modular design**.

---

## 🎯 Features

- **Add new books** with title, author, genre, and available copies.
- **Prevent duplicate book titles** (case-insensitive).
- **Borrow and return books**, updating available and borrowed status.
- **Remove books** from the library only if no copies are borrowed.
- **Display books** grouped by genre.
- **View an inventory summary** including total, available, and borrowed books.

---

## 🧠 Implemented Logic

- A `Library` class encapsulates all the logic and data related to books.
- A `utils.py` file centralizes input validations (strings, integers, genres).
- The program's flow is managed in `main.py`, with one handler function per action (e.g. `handle_add_book()`).
- Properties (`@property`) are used to dynamically compute total, available, and borrowed books.
- All book entries are stored as dictionaries in a list, using structured keys for consistency.

---

## ✅ Input Validations

- **Title** and **author**: must be non-empty and non-numeric.
- **Genre**: must be one of the valid predefined genres.
- **Copies**: must be a positive integer.
- Duplicate titles are not allowed (comparison is case-insensitive).
- Genres are validated against an accepted list.
- All user inputs are validated before being processed.

---

## 📁 Project Structure

```
library_app/
├── main.py       # User interface and menu handling
├── library.py    # Library class with all business logic
└── utils.py      # Input validation functions
```

---

## 🧩 File Descriptions

- **`main.py`**  
  Controls the application's menu and user input. Each menu option calls a dedicated function (`handle_add_book`, `handle_borrow_book`, etc.) for clarity and modularity.

- **`library.py`**  
  Defines the `Library` class. Handles book registration, validation, borrowing, returning, and removal. Includes book listings and inventory summary.

- **`utils.py`**  
  Provides reusable validation functions for strings, integers, and valid genres. Ensures clean and safe data input.

---

## 💡 Technical Highlights

- The use of `@property` provides real-time inventory insights (total, available, borrowed).
- Modular design allows easy maintenance and potential scalability.
- Input validation is centralized and robust.
- Clear naming conventions and structured dictionaries make data handling predictable.
- Prepared for future integration with GUIs or APIs.

---

## 🚀 Possible Future Enhancements

- Allow editing book details (title, author, genre).
- Add support for book descriptions or ISBN numbers.
- Implement filters by author or availability.
- Export/import book data from files (CSV, JSON).
- Integrate with a graphical UI using Tkinter or a web interface with Flask.

---

## 💻 How to Run

1. Make sure Python 3.10+ is installed.
2. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Library-Management.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Library-Management/library_app
   ```

4. Run the main script:

   ```bash
   python main.py
   ```

5. Use the interactive menu to manage the books in your library.

---
