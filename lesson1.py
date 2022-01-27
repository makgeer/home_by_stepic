a = input('Введите трехзначное число:\n')
b = 0
c = 1
for letter in a:
    b += int(letter)
    c *= int(letter)
print(b, c)
