from project.library import Library


class User:
    books = []

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def get_book(self, author, book_name, days_to_return, library: Library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            library.rented_books[self.username] = {book_name: 0}
            library.rented_books[self.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        if book_name in library.rented_books[self.username]:
            return f"The book '{book_name}' is already rented and will be available in {library.rented_books[self.username][book_name]} days!"

    def return_book(self, author, book_name, library: Library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        library.rented_books[self.username].pop(book_name)
        library.books_available[author].append(book_name)

    def info(self):
        sorted_books = sorted(self.books)
        return ', '.join(sorted_books)

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'


