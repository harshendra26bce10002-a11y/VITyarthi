# Library Management System

A simple command-line based **Library Management System** built in Python. It allows a user to manage a collection of books through a menu-driven interface — adding, viewing, searching, issuing, returning, deleting, and counting books.

## Features

- **Add Book** – Add a new book to the library collection.
- **View Books** – Display all books currently available in the library.
- **Search Book** – Check whether a specific book is available.
- **Issue Book** – Issue a book to a borrower (removes it from the available list).
- **Return Book** – Return a previously issued book (adds it back to the available list).
- **Delete Book** – Permanently remove a book from the collection.
- **Count Books** – Display the total number of books currently available.
- **Exit** – Close the application.

## Technologies Used

- **Language:** Python 3
- **Data Structure:** Python list (used to store book records in memory)
- **Interface:** Command-line (text-based menu)

## How to Run

1. Make sure Python 3 is installed on your system.
2. Save the script as `VITYARTHI_PROJECT.py`.
3. Open a terminal in the folder containing the file.
4. Run the program:
   ```
   python VITYARTHI_PROJECT.py
   ```
5. Follow the on-screen menu by entering a number (1–8) for the desired action.

## Sample Menu

```
LIBRARY MANAGEMENT SYSTEM
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return book
6. Delete book
7. Count books
8. Exit
Enter your choice:
```

## Project Structure

```
VITYARTHI_PROJECT.py   # Main Python script containing all program logic
```

## Limitations

- Data is stored only in memory (a Python list); all records are lost once the program is closed, since there is no file or database storage.
- Book titles are treated as plain strings, so duplicate titles and case-sensitivity are not specially handled.
- No separate tracking of who issued a book or issue/return dates.

## Future Enhancements

- Persist data using a file (CSV/JSON) or a database (e.g., SQLite).
- Track borrower details and due dates for issued books.
- Add unique book IDs to avoid duplicate-title conflicts.
- Build a graphical user interface (GUI) using Tkinter.
