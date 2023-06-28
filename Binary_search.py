from random import randint

def binary_search(n: list, value: int)-> int:
    l = 0
    r = len(n) - 1
    count = 0

    while l <= r:
        count += 1

        m = l + ((r-l)//2)
        if n[m] == value:
            return f'Найденное число: {n[m]}, Индекс: {m + 1}  проходок: {count}'
        if n[m] > value:
            r = m - 1
        else:
            l = m + 1
    return "Такого числа нет"

        
data = [i for i in range(-1231, 12123)]
for i in range(10):
    x = randint(-1200,12122)
    print(binary_search(data, x))
    