from random import randint

def merge_list(lst1, lst2) -> list:
    result = []
    value1 = 0
    value2 = 0

    
    while value1 < len(lst1) and value2 < len(lst2):
        if lst1[value1] > lst2[value2]:
            result.append(lst2[value2])
            value2 += 1
        else:
            result.append(lst1[value1])
            value1 += 1
    result += lst1[value1:] + lst2[value2:]

    return result


def split_and_merge_list(data: list) -> list:
    N1 = len(data) // 2
    a1 = data[:N1]
    a2 = data[N1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)
    
    return merge_list(a1, a2)

def test():
    for _ in range(100):
        items_test = [randint(-1000, 1000) for _ in range(100)]
        assert sorted(items_test) == split_and_merge_list(items_test)
    print('Succseful testing')


if __name__ == "__main__":
    test()