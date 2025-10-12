def useless(lst):
    return max(lst) / len(lst)

print(useless([3, 5, 7, 43, 33, 12]))
print(useless([-12.5, 123.01, 111, -4, 85.3, 12.11, -9.83]))
print(useless([-21.2, 313, 0, -5, 0, 0.12, 1234, -1.314, 894]))