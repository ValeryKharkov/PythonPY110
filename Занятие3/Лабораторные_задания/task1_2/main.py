OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, 'w') as file:  # TODO записать лесенку в файл
        for line in range(1, 11):
            file.write(f"{line * '*':>5}\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")


