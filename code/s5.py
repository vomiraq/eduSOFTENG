# Написать программу, которая позволяет вести список любимых фильмов 
# с сохранением в текстовый файл.

def dobavit_film(fail):
    film = input("Введите название фильма: ")
    with open(fail, "a", encoding="utf-8") as f:
        f.seek(0, 2)
        if f.tell() != 0:
            f.write("\n")
        f.write(film)
    print("Фильм добавлен!")


def posmotret_filmy(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            filmy = [line.strip() for line in f if line.strip()]
            print("Список любимых фильмов:")
            for i, film in enumerate(filmy, 1):
                print(f"{i}. {film}")
            print(f"Всего фильмов: {len(filmy)}")
    except FileNotFoundError:
        print("Файл с фильмами еще не создан.")

def glavny_menu():
    file = "s5.txt"
    while True:
        print("\n1. Добавить фильм\n2. Посмотреть все фильмы\n3. Выход")
        vibor = input("Выберите действие: ")
        if vibor == "1":
            dobavit_film(file)
        elif vibor == "2":
            posmotret_filmy(file)
        elif vibor == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

glavny_menu()