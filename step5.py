a = int(input(""))
b = int(input(""))
c = int(input(""))
if a < b < c or b < a < c:
    if a < b:
        print(c, a, b, sep='\n')
    else:
        print(c, b, a, sep='\n')
elif b < c < a or c < b < a:
    if b < c:
        print(a, b, c, sep='\n')
    else:
        print(a, c, b, sep='\n')
elif a < c < b or c < a < b:
    if a < c:
        print(b, a, c, sep='\n')
    else:
        print(b, c, a, sep='\n')
if a == b < c:
    print(c, b, a, sep='\n')
elif a == b > c:
    print(a, c, b, sep='\n')
if b == c < a:
    print(a, c, b, sep='\n')
elif b == c > a:
    print(b, a, c, sep='\n')
if a == c < b:
    print(b, a, c, sep='\n')
elif a == c > b:
    print(a, b, c, sep='\n')
if a == b == c:
    print(a, b, c, sep='\n')