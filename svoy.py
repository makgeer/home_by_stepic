def count_repeated_letter(string1):
    list1 = []

    for letter in string1:
        if string1.count(letter) >= 1:
            if letter not in list1:
                list1.append(letter)


    for item in list1:
        if item != "":
            print(item, string1.count(item))


count_repeated_letter(input())
