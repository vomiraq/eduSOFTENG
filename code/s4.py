ocenki1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
ocenki2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
ocenki3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def izmenit_ocenki(ocenki):
    novye_ocenki = []
    for ocenka in ocenki:
        if ocenka == 2:
            continue
        elif ocenka == 3:
            novye_ocenki.append(4)
        else:
            novye_ocenki.append(ocenka)
    return novye_ocenki

ocenki1 = izmenit_ocenki(ocenki1)
ocenki2 = izmenit_ocenki(ocenki2)
ocenki3 = izmenit_ocenki(ocenki3)

print(ocenki1)
print(ocenki2)
print(ocenki3)
