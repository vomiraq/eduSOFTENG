class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def info(self):
        status = "прочитана" if self.is_read else "не прочитана"
        return f"{self.title} ({self.year}) - {self.author}. Статус: {status}"

book2 = Book("Преступление и наказание", "Ф. Достоевский", 1866)
print(book2.info())
book2.mark_as_read()
print(book2.info())
