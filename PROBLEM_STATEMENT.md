# Problem Statement

## Title
**Library Management System using Python**

## Introduction
Libraries, whether in schools, colleges, or public institutions, need to keep track of the books they own, which books are currently available, and which have been issued to readers. When this is done manually (using registers), it becomes time-consuming, error-prone, and difficult to search or update records quickly.

## Problem
There is a need for a simple, computer-based system that can:
- Maintain a record of all books in the library.
- Allow quick addition and deletion of book records.
- Let users check the availability of a specific book.
- Track whether a book is issued or available by updating records when a book is issued or returned.
- Provide a quick count of the total number of books currently in stock.

## Objective
To design and develop a **menu-driven Library Management System** in Python that allows a librarian or user to perform basic library operations — adding, viewing, searching, issuing, returning, deleting, and counting books — through a simple text-based interface, without requiring any external database or advanced setup.

## Scope
- The system is intended for **single-session use**, where a user interacts with the program through the console.
- It manages book records using an in-memory data structure (a Python list).
- It does not include user authentication, borrower history, or persistent storage in its current version, but is designed to be simple to extend later.

## Proposed Solution
A Python console application that presents the user with a numbered menu of operations. Based on the user's choice, the corresponding function logic executes:
1. Add a book to the collection.
2. View the full list of available books.
3. Search for a specific book by name.
4. Issue a book (remove it from the available list).
5. Return a book (add it back to the available list).
6. Delete a book permanently from records.
7. Count the total number of books available.
8. Exit the application.

## Expected Outcome
A working Python program that fulfills all the basic requirements of a small-scale library management workflow, demonstrating the use of loops, conditional statements, functions/lists, and user input handling in Python.
