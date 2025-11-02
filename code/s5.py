class Reader:
    def describe(self):
        return "Я читаю книги."

class Student(Reader):
    def describe(self):
        return "Я читаю учебники."

class Professor(Reader):
    def describe(self):
        return "Я читаю научные статьи."

people = [Reader(), Student(), Professor()]
for person in people:
    print(person.describe())