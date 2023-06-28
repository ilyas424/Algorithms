from random import randint

def binary_search(n: list, value: int)-> int:
    count = 0

    result = 0

    while len(n) != 1:
        count += 1

        k = len(n) // 2
        if n[k] == value:
            result = n[k]
            break
        if value > n[k]:
            n = n[k:]
        else:
            n = n[:k]

    if n[0] == value:
        result = n[0]

    if result == value:
        return f'Найденное число: {result},  проходок: {count}'
    else:
        return "Такого числа нет"
        
data = [i for i in range(-1232, 12123)]
for i in range(10):
    x = randint(-1200,12122)
    print(x)
    print(binary_search(data, x))
    