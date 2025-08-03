from library import Library

def main():
    lib = Library()

    while True:
        print("\n📚 Library Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Show all books")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            title = input("Book title: ")
            author = input("Author name: ")
            lib.add_book(title, author)

        elif choice == '2':
            title = input("Book title to remove: ")
            lib.remove_book(title)

        elif choice == '3':
            title = input("Book title to search: ")
            lib.search_book(title)

        elif choice == '4':
            lib.show_books()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")

        print("-" * 40)  

if __name__ == "__main__":
    main()
