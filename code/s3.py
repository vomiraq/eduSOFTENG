def stat_text(fail):
    with open(fail, encoding='utf-8') as f:
        text = f.read()
        lines = text.splitlines()
        num_lines = len(lines)
        words = text.split()
        num_words = len(words)
        num_letters = sum(1 for c in text if c.isalpha() and c.isascii())
        print("Input file contains:")
        print(f"{num_letters} letters")
        print(f"{num_words} words")
        print(f"{num_lines} lines")

stat_text("s3.txt")
