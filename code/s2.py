def dobavit_rasxod(file):
    kategorii = input("Введите категорию расхода: ")
    summa = input("Введите сумму расхода: ")
    opisanie = input("Введите описание расхода: ")
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{kategorii};{summa};{opisanie}\n")
    print("Расход добавлен!")

def posmotret_rasxody(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            print("Существующие расходы:")
            for line in f:
                kategorii, summa, opisanie = line.strip().split(";")
                print(f"Категория: {kategorii}, Сумма: {summa}, Описание: {opisanie}")
    except FileNotFoundError:
        print("Файл с расходами еще не создан.")

def glavnyy_menu():
    file = "s2.txt"
    while True:
        print("\n1. Добавить расход\n2. Посмотреть все расходы\n3. Выход")
        vibor = input("Выберите действие: ")
        if vibor == "1":
            dobavit_rasxod(file)
        elif vibor == "2":
            posmotret_rasxody(file)
        elif vibor == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

glavnyy_menu()
