choos = input("")
if choos == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    d = 0.5 * (a + b + c)
    print((d * (d - a) * (d - b) * (d - c)) ** 0.5)
elif choos == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a * b)
elif choos == "круг":
    a = int(input())
    print(3.14 * (a ** 2))
    