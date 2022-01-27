a = input()
cnt = 0
if 'c' or 'g' in a:
    cnt = a.upper().count('c'.upper()) + a.upper().count('g'.upper())
print(cnt / len(a) * 100)
