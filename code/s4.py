def calculate_average(*args):
    if len(args) == 0:
        print("Ошибка: не передано ни одного аргумента")
        return None
    total_sum = sum(args)
    count = len(args)
    average = total_sum / count
    
    print(f"Передано аргументов: {count}")
    print(f"Аргументы: {args}")
    print(f"Сумма аргументов: {total_sum}")
    print(f"Среднее арифметическое: {average:.2f}")
    
    return average

if __name__ == "__main__":
    
    print("Пример 1:")
    calculate_average(1, 2, 3, 4, 5)
    
    print("\nПример 2:")
    calculate_average(10, 20, 30)
    
    print("\nПример 3:")
    calculate_average(2.5, 3.7, 1.8, 4.2)
    
    print("\nПример 4 (один аргумент):")
    calculate_average(7)
    
    print("\nПример 5 (без аргументов):")
    calculate_average()