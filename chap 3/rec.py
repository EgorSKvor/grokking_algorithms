def factorial(num: int):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
# рекурсия - когда функция вызывает себя в функции


print(factorial(3))
