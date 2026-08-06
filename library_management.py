books = []

while True:
    print("\n========== MINI LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        books.append({
            "Title": title,
            "Author": author
        })

        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("Library is empty.")
        else:
            print("\n------ BOOK LIST ------")
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book['Title']} by {book['Author']}")

    elif choice == "3":
        search = input("Enter book title to search: ").lower()

        found = False

        for book in books:
            if book["Title"].lower() == search:
                print("\nBook Found!")
                print("Title :", book["Title"])
                print("Author:", book["Author"])
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        remove = input("Enter book title to remove: ").lower()

        found = False

        for book in books:
            if book["Title"].lower() == remove:
                books.remove(book)
                print("Book removed successfully!")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
        