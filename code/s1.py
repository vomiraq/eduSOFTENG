class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Книга: {self.title}, Автор: {self.author}"

book1 = Book("Мастер и Маргарита", "М. Булгаков")
print(book1.info())
