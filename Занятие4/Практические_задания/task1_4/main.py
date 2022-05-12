import re


def task():
    date_str = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

    date_pattern = re.compile(r"(?P<day>\d\d)-(?P<mounth>\d\d)-(?P<year>\d{4})")  # записать регулярное выражение с именованными группами
    for date in date_pattern.finditer(date_str):  # итератор по совпадениям
        print(date.groupdict())  # вернуть словарь с именованными группами
        print('------')


if __name__ == "__main__":
    task()
