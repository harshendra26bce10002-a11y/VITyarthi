books=[]
#empty book list
while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3.Search Book")
    print("4.Issue Book")
    print("5. Return book")
    print("6. Delete book")
    print("7. Count books")
    print("8. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        book=input("Enter book name: ")
        books.append(book)
        print("book get added successfully")
    elif choice == '2':
        if len(books) == 0:
            print("No books available")
            #in case when there is no book available in the library
        else:
            print(" Following Books are available:")
            for book in books:
                print(book)
    elif choice == '3':
        search_book=input("Enter book name to search: ")
        if search_book in books:
            print("Book is available in the library")
        else:
            print("Book is not available in the library")
    elif choice == '4':
        issue_book=input("Enter book name to issue: ")
        if issue_book in books:
            books.remove(issue_book)
            #book will be removed from the list of available books when it is issued
            print("Book issued successfully")
        else:
            print("Book is not available")
    elif choice == '5':
        return_book=input("Enter book name to return: ")
        books.append(return_book)
        #book will be added back to the list of available books when it is returned
        print("Book returned successfully")
    elif choice == '6':
        delete_book=input("Enter book name to delete: ")
        if delete_book in books:
            books.remove(delete_book)
            #book will be removed from the list of available books when it is deleted
            print("Book deleted successfully")
        else:
            print("Book is not available")
    elif choice == '7':
        print("Total number of books available in the library:", len(books))
        #counting the total number of books available in the library
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        
