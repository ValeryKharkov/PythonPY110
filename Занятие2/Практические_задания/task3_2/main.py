import time


def time_decorator(fn):
    print("Этот код будет выведен в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")

        t0 = time.time()  # зафиксировать время до начала выполнения функции
        print(t0)
        result = fn(*args, **kwargs)
        time.sleep(3)  # это костыль: добавили засыпание, что бы увидеть разницу во времени
        print(result)
        dt = time.time() - t0  # зафиксировать время после выполнения
        print(dt)

        print("Этот код будет выполняться после каждого вызова функции")
        return result
    return wrapper


@time_decorator  # задекорировать функцию
def pow_(a, n):
    return pow(a, n)


if __name__ == "__main__":
    print(pow_)
    print("=" * 25)

    print(pow_(5, 2))
    print("=" * 25)

    print(pow_(4, 4))
