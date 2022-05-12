import re

string = 'Everest is the largest mountain in the World'

# pattern = r'.'  # Вытащить каждый символ из строки
# pattern = r'\w'  # Сделать, что бы в конечный результат не попадал пробел
# pattern = r'\w*\S'  # Достать слова с помощью * или +
# pattern = r'\w+'  # Достать слова с помощью * или +
pattern = r'\b[aeiouAEIOU]\w+'  # Извлечь слова начинающиеся на гласную

result = re.findall(pattern, string)
print(result)

