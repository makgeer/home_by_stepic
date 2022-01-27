a = ['программист', 'программиста', 'программистов']
b = input()
s_list = list(b)
if len(s_list) == 1:
    if int(s_list[0]) == 0:
        print(f'{b} {a[2]}')
    elif int(s_list[0]) == 1:
        print(f'{b} {a[0]}')
    elif int(s_list[0]) < 5:
        print(f'{b} {a[1]}')
    elif int(s_list[0]) > 4:
        print(f'{b} {a[-1]}')

if len(s_list) == 2:
    if int(s_list[-1]) == 0:
        print(f'{b} {a[2]}')
    elif int(s_list[0]) == 1 and int(s_list[-1]) > 0:
        print(f'{b} {a[-1]}')
    elif int(s_list[0]) > 1 and int(s_list[-1]) == 1:
        print(f'{b} {a[0]}')
    elif int(s_list[1]) > 1 and int(s_list[-1]) < 5:
        print(f'{b} {a[1]}')
    elif int(s_list[-1]) > 4:
        print(f'{b} {a[-1]}')

if len(s_list) >= 3:

    if int(s_list[-1]) == 0:
        print(f'{b} {a[2]}')

    elif int(s_list[1]) == 0 and int(s_list[-1]) == 1:
        print(f'{b} {a[0]}')

    elif int(s_list[-2]) == 0  and int(s_list[-1]) < 5:
        print(f'{b} {a[1]}')

    elif int(s_list[-2]) == 0 and int(s_list[-1]) > 4:
        print(f'{b} {a[-1]}')

    elif int(s_list[-2]) == 1 and int(s_list[-1]) > 0:
        print(f'{b} {a[-1]}')

    elif int(s_list[-2]) > 1 and int(s_list[-1]) == 1:
        print(f'{b} {a[0]}')

    elif int(s_list[-2]) >1 and int(s_list[-1]) < 5:
        print(f'{b} {a[1]}')
    elif int(s_list[-2]) >1 and int(s_list[-1]) > 4:
        print(f'{b} {a[-1]}')
