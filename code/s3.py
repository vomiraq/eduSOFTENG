def top3_digits(s):
    counts = {}
    for ch in s:
        digit = int(ch)
        if digit in counts:
            counts[digit] += 1
        else:
            counts[digit] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_counts[:3]
    result = dict(sorted(top3, key=lambda x: x[0]))
    return result

s = "123456789012345"
print(top3_digits(s))
