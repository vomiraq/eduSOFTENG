def otbor_studentov(spisok_studentov, porog):
    rezultaty = []
    for student in spisok_studentov:
        imya, ocenki = student
        srednee = sum(ocenki) / len(ocenki)
        if srednee >= porog:
            rezultaty.append((imya, srednee))
    rezultaty.sort(key=lambda x: x[1], reverse=True)
    itog = [imya for imya, _ in rezultaty]
    return itog

# тесты

studenty = [
    ("Иван", [5, 4, 5, 5]),
    ("Анна", [3, 4, 4, 3]),
    ("Петя", [5, 5, 4, 5]),
    ("Ольга", [2, 3, 3, 4]),
    ("Саша", [4, 4, 5, 4])
]

print(otbor_studentov(studenty, 4.5))
print(otbor_studentov(studenty, 4.0))
print(otbor_studentov(studenty, 3.5))

# Напишите программу, которая принимает список студентов, представленных 
# в виде кортежей `(имя, [оценки])`, вычисляет средний балл каждого студента
# и отбирает тех, чей средний балл не ниже заданного порога. Результатом
# должна быть отсортированная по убыванию среднего балла последовательность
# имён студентов, прошедших отбор.
