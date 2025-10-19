def remove1st(tuple1, elm):
    list1 = list(tuple1)

    if elm in list1:
        list1.remove(elm)
    return tuple(list1)

print(remove1st((1, 2, 3), 1))
print(remove1st((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove1st((2, 4, 6, 6, 4, 2), 9))