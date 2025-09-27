str = input('Введите предложение: ')
print('Длина предложения: ', len(str))
str_down = str.lower()
print('Перевод в нижний регистр: ', str_down)
count = str_down.count('a') + str_down.count('e') + str_down.count('i') \
    + str_down.count('o') + str_down.count('u')
print('Количество гласных: ', count)
zamena = str.replace('ugly', 'beauty')
print('Замена ugly на beauty: ', zamena)
if str.startswith('The') and str.endswith('end'):
    print('Предложение начинается на The и заканчивается на end')
else:
    print('Предложение не начинается на The и не заканчивается на end')
                                                          