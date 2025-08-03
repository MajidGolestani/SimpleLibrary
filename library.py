



class Library():
    def __init__(self):
        self.books = []

    def add_book(self, title, author):

        book = {'title': title, 'author': author}
        self.books.append(book)
        print(f'book {title} by {author} added.')

    def remove_book(self, title):

        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                print(f'book {title} deleted')
                return
        print(f'book {title} not found.')

    def search_book(self, title):
        for book in self.books:
            if book['title'] == title:
                print(f'book {title} founded.')
                return book
        print(f'book {title} not found.')
        return None
    
    def show_books(self):
        if not self.books:
            print("there isn't any book in the library.")
        else:
            print("all books in library")
        for book in self.books:
            print(f'book is {book['title']} and author is {book['author']}.')
    



        