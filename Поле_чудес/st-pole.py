import tkinter as tk
import random
from tkinter import messagebox


def choose_word(words):
    return random.choice(words)


word_list = ["PROGRAMMING", "COMPUTER", "MATH", "LANGUAGE", "BOOK", "PYTHON", "APPLE"]
word = choose_word(word_list)


def get_status(word, guesses):
    status = ""
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "_"
    return status


def check_word(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    return True


def guess_letter():
    letter = letter_entry.get()
    letter_entry.delete(0, tk.END)
    if letter.isalpha() and len(letter) == 1:
        if letter in guesses:
            status_label.config(text="Ця лiтера вже використана!")
        else:
            guesses.append(letter)
            status = get_status(word, guesses)
            status_label.config(text=status)
            if check_word(word, guesses):
                status_label.config(text="Ви виграли!")
                letter_entry.config(state=tk.DISABLED)
            elif len(guesses) == n:
                status_label.config(text="Ви програли! Загадане слово: " + word)
                letter_entry.config(state=tk.DISABLED)
    else:
        status_label.config(text="Неправильний ввiд!")


allowed_errors = len(word)


def update_status(word, guesses):
    status = ""
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "_ "
    status_label.config(text=status)


def guess_letter():
    letter = letter_entry.get().upper()
    if letter.isalpha() and len(letter) == 1:
        if letter in guesses:
            tk.messagebox.showwarning("Помилка", "Ця літера вже використана.")
        elif letter in word:
            guesses.append(letter)
            update_status(word, guesses)
            used.append(letter)
            used_label.config(text=f"Ви використали наступні літери: {', '.join(used)}")
            if check_word(word, guesses):
                status_label.config(text="Ви виграли!")
                letter_entry.config(state=tk.DISABLED)
        else:
            guesses.append(letter)
            allowed = allowed_errors - len(guesses)
            if allowed == 0:
                status_label.config(text=f"Ви програли. Секретне слово: {word}")
                letter_entry.config(state=tk.DISABLED)
            else:
                update_status(word, guesses)
                used.append(letter)
                used_label.config(
                    text=f"Ви використали наступні літери: {', '.join(used)}\nУ Вас залишилося {allowed} спроб.")
    else:
        tk.messagebox.showwarning("Помилка", "Будь ласка, введіть одну букву.")


def check_word(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    return True


window = tk.Tk()
window.title("Поле чудес")
window.geometry("500x300")

# Create status label
status_label = tk.Label(window, text="_ " * len(word), font=("Arial", 16))
status_label.pack(pady=10)

# Create label for used letters
used_label = tk.Label(window, text="Ви ще не використали жодної літери.", font=("Arial", 12))
used_label.pack(pady=5)

letter_entry = tk.Entry(window, font=("Arial", 12))
letter_entry.pack(pady=5)
guess_button = tk.Button(window, text="Відгадати", command=guess_letter)
guess_button.pack(pady=5)

guesses = []
used = []


def guess_letter():
    letter = letter_entry.get().upper()

    letter_entry.delete(0, tk.END)

    if letter in used:
        messagebox.showwarning("Увага!", "Ви вже використали цю літеру. Спробуйте іншу.")
    else:

        used.append(letter)

        if letter in word:

            guesses.append(letter)

            update_status(word, guesses)

            if check_word(word, guesses):
                status_label.config(text="Ви виграли!")
                letter_entry.config(state=tk.DISABLED)
        else:

            remaining_guesses = len(word) - len(guesses)
            remaining_guesses -= 1

            update_status(word, guesses)

            if remaining_guesses == 0:
                status_label.config(text="Ви програли. Слово було '{}'.".format(word))
                letter_entry.config(state=tk.DISABLED)


window.mainloop()

word = choose_word(word_list)
guesses = []
n = len(word)

status = get_status(word, guesses)
status_label = tk.Label(window, text=status, font=("Helvetica", 20))
status_label.pack(pady=10)

letter_entry = tk.Entry(window, font=("Helvetica", 16))
letter_entry.pack(pady=5)
letter_entry.focus()

status_label = tk.Label(window, text="", font=("Helvetica", 12))
status_label.pack(pady=10)


def update_status(word, guesses, attempts_left):
    hidden = ""
    for letter in word:
        if letter in guesses:
            hidden += letter + " "
        else:
            hidden += "_ "

    if "_" not in hidden:
        status_label.config(text="Ви виграли!")
        letter_entry.config(state=tk.DISABLED)
    elif attempts_left == 0:
        status_label.config(text=f"Ви програли. Загадане слово було '{word}'.")
        letter_entry.config(state=tk.DISABLED)


def check_word(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    return True


def guess_letter():
    letter = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if len(letter) != 1:
        status_label.config(text="Введіть тільки одну літеру.")
        return

    if not letter.isalpha():
        status_label.config(text="Введіть літеру.")
        return

    if letter in guesses:
        status_label.config(text="Ця літера вже була відгадана.")
        return

    guesses.append(letter)

    update_status(word, guesses)

    if check_word(word, guesses):
        status_label.config(text="Ви виграли!")
        letter_entry.config(state=tk.DISABLED)
        guess_button.config(state=tk.DISABLED)

    elif len(guesses) >= len(word):
        status_label.config(text=f"Ви програли. Загадане слово: {word}")
        letter_entry.config(state=tk.DISABLED)
        guess_button.config(state=tk.DISABLED)
    else:
        status_label.config(
            text=f"Ви використали наступні літери: {' '.join(guesses)} У вас залишилось {len(word) - len(guesses)} спроб.")