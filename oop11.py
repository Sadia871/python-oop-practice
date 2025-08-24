class Book:
    def __init__(self, title, author, price , name):
        self.title = title
        self.author = author
        self.price = price
        self.name = name

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price}, Name: {self.name}"
book = Book("1984", "George Orwell", 15.99, "The Art of Being Alone")
print(book.display_info())