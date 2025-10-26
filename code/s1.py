def analiz_texta(file):
    with open(file, encoding='utf-8') as f:
        text = f.read().lower()
        
        for simbol in ",.!?;:-\"()\n":
            text = text.replace(simbol, " ")
        slova = text.split()
        kolichestvo_slov = len(slova)
        chastota = {}
        
        for slovo in slova:
            chastota[slovo] = chastota.get(slovo, 0) + 1
        chastoe_slovo = max(chastota, key=chastota.get)
        skolko_raz = chastota[chastoe_slovo]
        
        print(f"Количество слов в файле: {kolichestvo_slov}")
        print(f"Самое частое слово: '{chastoe_slovo}' — встречается {skolko_raz} раз(а)")

analiz_texta("s1.txt")
