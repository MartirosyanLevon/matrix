from random import randint

a = []
n = int(input('Enter size of row: '))
s = int(input('Enter size of column: '))


for i in range(n):
    b = []
    for i in range(s):
        #b.append(int(input('Enter numbre: ')))    # user version
        b.append(randint(0,100))                  # random version
    a.append(b)


for i in a:
    print((i))