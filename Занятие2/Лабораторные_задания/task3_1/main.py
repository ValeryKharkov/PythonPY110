def positive_check(fn):
    def wrapper(arg):
        if not arg > 0:  # написать проверку положительности аргумента arg
            raise ValueError("Аргумент функции не является положительным числом")

        result = fn(arg)
        return result


    return wrapper


@positive_check  # задекорировать функцию
def some_func(num: int):
    return num


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
