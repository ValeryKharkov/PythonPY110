def count(start_number: float = 1, step: float = 1):
# Записать свою версию итератора чисел из бесконечной арифметической прогрессии.
    while True:
        yield start_number
        start_number += step

if __name__ == "__main__":
    my_count = count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
