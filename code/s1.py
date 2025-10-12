visits = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
          1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
          5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
          5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
          3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

visits_count = len(visits)
print("Сколько было выдано чеков: ", visits_count)

unique_visits = len(set(visits))
print("Сколько разных людей посетило ресторан: ", unique_visits)

visit_counts = {}

for code in visits:
    if code in visit_counts:
        visit_counts[code] += 1
    else:
        visit_counts[code] = 1

max_visits = 0
most_common_person = None

for code in visit_counts:
    if visit_counts[code] > max_visits:
        max_visits = visit_counts[code]
        most_common_person = code

print("Какой работник посетил ресторан больше всех раз: ", most_common_person)