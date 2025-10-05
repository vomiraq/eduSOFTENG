import random

def kost():
    znach = random.randint(1, 6)
   
    print(f"Выпало: {znach}")
    
    if znach == 5 or znach == 6:
        print("Вы победили")
    elif znach == 3 or znach == 4:
        print("Повторный бросок")
        kost()
    elif znach == 1 or znach == 2:
        print("Вы проиграли")

if __name__ == "__main__":
    kost()