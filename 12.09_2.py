#2. Выбрать (в виде списка) из текста все слова, в которых встречаются, как русские,
# так и латинские буквы (типичная ошибка, когда вместо русской буквы печатается латинская
# с тем же начертанием, особенно с/c – расположены на одной кнопке русскоязычной клавиатуры).
# Словом считается непрерывная последовательность символов (строчных и прописных) А-Я, A-Z и цифр.
import re

def check_words(word):
    for c in set(word):
        if word.count(c):
            return True
    return False

def filter(words):
    return [word for word in words if check_words(word)]



if __name__ == '__main__':
    text = "я текст тутjвв дддGGGjd"
    print(text)

    pattern = r"\b(?=\w*[a-zA-Z])(?=\w*[а-яА-Я])[а-яА-Яa-zA-Z]+\b"
    matches = re.findall(pattern, text)
    print(matches)

