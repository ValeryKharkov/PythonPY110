INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as f:  # открыть указатель на файл
        for line in f:  # файл является итератором, который работает с циклом for в построчном режиме
            line = line.strip('\n')
            print(line)

if __name__ == "__main__":
    task()

