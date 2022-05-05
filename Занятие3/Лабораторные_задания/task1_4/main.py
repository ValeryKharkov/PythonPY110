INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def input_lines():
    with open(INPUT_FILE, 'r') as file:
        data = file.read()

        return data.upper()


def task():
    with open(OUTPUT_FILE, 'w') as file:  # TODO перезаписать содержимое одного файла в другой
        file.write(input_lines())

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")

