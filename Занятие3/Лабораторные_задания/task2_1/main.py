import json


def task() -> str:
    dict_numbers = {n: n ** 2 for n in range(1, 11)}  # c помощью dict comprehension сформировать словарь
    return json.dumps(dict_numbers, indent=4) # сеализовать словарь в JSON строку


if __name__ == "__main__":
    print(task())

'''
item = {n: n*2 for n in range(10)}
print(item)

def to_json_string(python_object) -> str:
    json_string = json.dumps(python_object)  # метод dumps сериализует объект в JSON строку
    return json_string

'''