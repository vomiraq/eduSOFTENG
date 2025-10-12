list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def form_set(lst):
    result_set = set()
    for number in set(lst):
        count = lst.count(number)
        for i in range(1, count + 1):
            if i == 1:
                result_set.add(number)
            else:
                result_set.add(str(number) * i)
    return result_set

print(form_set(list_1))
print(form_set(list_2))
print(form_set(list_3))
