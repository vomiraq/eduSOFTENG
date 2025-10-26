#lines = ['stroka1', 'stroka2']
#with open('l6.txt', 'w') as f:
#    for line in lines:
#        f.write(line + '\n')

lines = ['one', 'two', 'three']
with open('l6.txt', 'w') as f:
    for line in lines:
        f.write('Cycle run ' + line + '\n')
    print('Done!')