# Task 1: Library System Enhancement

def add_new_book(library):
    title = input("Enter the book's title to add: ")
    author = input("Enter the author: ")
    book = (title, author)
    if book in library:
        print("Book already exists in library.")
    else:
        library.append(book)
        print(f"New book '{title}' by {author} has been added to the library.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_new_book(library)