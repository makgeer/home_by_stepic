a = [int(i) for i in input().split()]
a.sort()
c = []
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        if a[i] not in c:
            c.append(a[i])
for i in range(0, len(c)):
    print(c[i], end=' ')
