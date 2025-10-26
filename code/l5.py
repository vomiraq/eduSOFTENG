with open('l5.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('l5.txt', 'r') as f:
    result = f.readlines()
    print(result)