class Book:
    def __init__(self, content):
        self.content = content


class Formatter:
    def format(self, book):
        return book.content


class TrimContentFormatter:
    def format(self, book):
        return book.content[:3]


class Printer:
    def get_book(self, book, formatter):
        return formatter.format(book)


book = Book('pages')
print(Printer().get_book(book, Formatter()))
print(Printer().get_book(book, TrimContentFormatter()))




