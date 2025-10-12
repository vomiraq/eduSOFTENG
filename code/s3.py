import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_a = max(one)
max_b = max(two)
max_c = max(three)

min_a = min(one)
min_b = min(two)
min_c = min(three)

p_max = (max_a + max_b + max_c) / 2
S_max = math.sqrt(p_max * (p_max - max_a) * (p_max - max_b) * (p_max - max_c))

p_min = (min_a + min_b + min_c) / 2
S_min = math.sqrt(p_min * (p_min - min_a) * (p_min - min_b) * (p_min - min_c))

print("Площадь треугольника с максимальными сторонами:", S_max)
print("Площадь треугольника с минимальными сторонами:", S_min)
