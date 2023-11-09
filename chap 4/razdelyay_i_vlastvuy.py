def summ(mas):
    if len(mas) == 0:
        return 0
    elif len(mas) == 1:
        return mas[0]
    else:
        f_el = mas[0]
        mas.pop(0)
        return f_el + summ(mas)


mass = [1, 2, 3, 4]
# print(len(mass))
print(summ(mass))
