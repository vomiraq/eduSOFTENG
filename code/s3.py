class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def info(self):
        return f"Электронная книга: {self.title} - {self.author}, размер файла: {self.file_size} МБ"

ebook = EBook("1984", "Джордж Оруэлл", 2.5)
print(ebook.info())
