x = input().split()#строка с числами разделенными пробелами на вход
if len(x) == 1:
    print(x[0])
elif len(x) > 1:# создаю новый список
    y = [int(x[i-1])+int(x[i+1]) for i in range(-1, len(x)-1)]
    for i in range(1, len(y)):
        print(y[i], end=' ')#вывожу значения со второго до последнего
    print(y[0])#вывожу первое значение