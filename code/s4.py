def zamena_zapreshennyh(file, text):
    with open(file, encoding='utf-8') as f:
        zapr_words = f.read().lower().split()

    text_low = text.lower()
    mask = list(text)

    for zapr in zapr_words:
        start = 0
        while True:
            index = text_low.find(zapr, start)
            if index == -1:
                break
            for i in range(index, index + len(zapr)):
                mask[i] = '*'
            start = index + 1

    print("".join(mask))


proverka_text = """Hello, world! Python IS the programming language of the future. My EMAIL is....
PYTHON is awesome!!!!"""

zamena_zapreshennyh("s4.txt", proverka_text)
