def pow_gen(base: int):
    num = 0
    while True:
        yield base ** num  # записать функцию-генератор
        num += 1

if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
