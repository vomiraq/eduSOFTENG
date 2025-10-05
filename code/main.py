from calc import triangle_area

a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))

result = triangle_area(a, b, c)
print(f"Площадь треугольника: {result}")