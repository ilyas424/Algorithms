from random import randint

def insertion_sort(lst: list)-> list:

    for i in range(1, len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1],  lst[j]
            j -= 1
    return lst


def test():

    for _ in range(10000):
        data = [randint(-1000, 1000) for _ in range(10)]
        assert sorted(data) == insertion_sort(data)
    assert [1]  == insertion_sort([1])
    assert [] == insertion_sort([])
    assert [0.2, 1.5, 2.1, 2.5] == insertion_sort([1.5, 0.2, 2.5, 2.1])
    print(f'😊 tests successful')


if __name__ ==  "__main__":
    test()