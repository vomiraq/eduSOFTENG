class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_info(self):
        return f"{self.__title} - {self.__author}"

    def set_title(self, new_title):
        self.__title = new_title

book = Book("Тихий Дон", "М. Шолохов")
print(book.get_info())
book.set_title("Поднятая целина")
print(book.get_info())
