def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return max(map(len, list_words))  # найти длину самого длинного слова


if __name__ == "__main__":
    print(task())
