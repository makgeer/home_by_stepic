n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print('Sololearn')
    elif x % 3 == 0 and x % 2 == 1:
        print('Solo')
    elif x % 5 == 0 and x % 2 == 1:
        print('Learn')
    else:
        if x % 2 == 1:
            print(x)
