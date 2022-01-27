a = float(input(""))
b = float(input(""))
s = input("")
if s in ('+', '-', '/', '*', 'mod', 'pow', 'div'):
    x = a
    y = b
    if s == '+':
        print(x + y)
    elif s == '-':
        print(x - y)
    elif s == '*':
        if x == -x or y == -y:
            print((-x) * (-y) or x * (-y) or (-x) * y)
        else:
            print(x * y)
    elif s == '/':
        if y != 0:
            print(x / y)
        else:
            print("Деление на 0!")
    elif s == 'mod':
        if y != 0:
            print(x % y)
        else:
            print("Деление на 0!")
    elif s == 'pow':
        if x == -x or y == -y:
            print((-x) ** (-y) or x ** (-y) or (-x) ** y)
        else:
            print(x ** y)
    elif s == 'div':
        if y != 0:
            print(x // y)
        else:
            print("Деление на 0!")
