# Class library
# Layers of Abstraction -> list available books, add book, lend book
class Library:
    def __init__(self):
        self.available_books = []
        pass

    def list_available_books(self):
        pass

    def add_book(self):
        pass

    def lend_book(self):
        pass

# Class Customer
# Layers of Abstraction -> return book, request book
# Customer có thể return book hoặc request book
# Customer không cần biết Library làm gì, chỉ cần biết là có thể return book hoặc request book
# Customer chỉ cần biết là có thể gọi các method của Library để thực hiện các hành động đó
class Customer:
    def return_book(self):
        pass

    def request_book(self):
        pass