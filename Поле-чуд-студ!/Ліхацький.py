import random

# список таємних слів
secret_words = ["home", "code", "word", "class"]

# обираємо таємне слово
secret_word = random.choice(secret_words)

# довжина таємного слова
word_length = len(secret_word)

# допустима кількість помилок
max_errors = word_length

# список вгаданих літер
guessed_letters = []

# кількість помилок, які залишилися
remaining_errors = max_errors

while True:
    # виводимо інформацію
    print("=" * 62)
    print(" " * 26 + "Поле чудес")
    print("=" * 62)
    print(" ".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
    print("=" * 62)
    print(f"Ви використали наступні літери: {' '.join(guessed_letters)}")
    print(f"У вас залишилося в {remaining_errors} спроб")
    print("=" * 62)

    # перевіряємо, чи закінчилися спроби
    if remaining_errors == 0:
        print(f"Ви програли. Таємне слово було '{secret_word}'")
        break

    # запитуємо користувача наступну літеру
    letter = input("Введіть літеру: ").lower()

    # перевіряємо, чи введено одну літеру
    if len(letter) != 1 or not letter.isalpha():
        print("Введіть одну літеру")
        continue

    # перевіряємо, чи літера вже була вгадана
    if letter in guessed_letters:
        print("Цю літеру вже використано")
        continue

    # додаємо вгадану літеру до списку
    guessed_letters.append(letter)

    # перевіряємо, чи вгадана літера є в таємному слові
    if letter not in secret_word:
        remaining_errors -= 1
        print(f"Літера '{letter}' відсутня в таємному слові")
        continue

    # перевіряємо, чи всі літери вгадані
    if all(letter in guessed_letters for letter in secret_word):
        print(f"Вітаємо! Ви вгадали таємне слово '{secret_word}'")
        break