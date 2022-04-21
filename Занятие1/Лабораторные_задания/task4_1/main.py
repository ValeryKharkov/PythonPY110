from itertools import count


def task():
    counter = count(100, 10)

    for i in range(10):
        print(next(counter))# распечатать с столбик первые 10 чисел бесконечного итератора


if __name__ == "__main__":
    task()
