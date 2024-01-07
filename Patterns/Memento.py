"""
Програма на Python з використанням патерну "Мементо" (Memento).
В цій програмі ми створимо класи для розробки текстового редактора,
який дозволяє зберігати та відновлювати стани текстового документа
за допомогою мементо.
"""

# Клас Мементо
# class Memento:
#     def __init__(self, state):
#         self.state = state
#
#     def get_state(self):
#         return self.state
#
#
# # Клас Опікун (Caretaker)
# class Caretaker:
#     def __init__(self):
#         self.mementos = []
#
#     def add_memento(self, memento):
#         self.mementos.append(memento)
#
#     def get_memento(self, index):
#         return self.mementos[index]
#
#
# # Клас Зберігач (Originator)
# class TextEditor:
#     def __init__(self):
#         self.text = ""
#
#     def set_text(self, text):
#         self.text = text
#
#     def get_text(self):
#         return self.text
#
#     def create_memento(self):
#         return Memento(self.text)
#
#     def restore_from_memento(self, memento):
#         self.text = memento.get_state()
#
#
# # Приклад використання
# if __name__ == "__main__":
#     caretaker = Caretaker()
#     text_editor = TextEditor()
#
#     text_editor.set_text("Hello, World!")
#
#     # Зберегти поточний стан
#     caretaker.add_memento(text_editor.create_memento())
#
#     text_editor.set_text("This is a new text.")
#
#     # Зберегти новий стан
#     caretaker.add_memento(text_editor.create_memento())
#
#     text_editor.set_text("Ukraine is the best!")
#     caretaker.add_memento(text_editor.create_memento())
#
#     # Відновити попередній стан
#     text_editor.restore_from_memento(caretaker.get_memento(0))
#
#     print("Current text:", text_editor.get_text())  # Виведе "Hello, World!"
#
#     # Відновити попередній стан
#     text_editor.restore_from_memento(caretaker.get_memento(-1))
#
#     print("Current text:", text_editor.get_text())  # Виведе "Ukraine is the best!"
#
#     # Відновити попередній стан
#     text_editor.restore_from_memento(caretaker.get_memento(1))
#
#     print("Current text:", text_editor.get_text())  # This is a new text."
#
#     # list1 = [1, 0, 2, 1, 2, 0, 1]
#     #
#     # for index in list1:
#     #     print('.' * 80)
#     #     text_editor.restore_from_memento(caretaker.get_memento(index))
#     #     print(f"Current text:", text_editor.get_text())
#


"""
У цій програмі є три класи:

Memento представляє об'єкт-мементо, 
який зберігає стан текстового документа.

Caretaker - це опікун, який зберігає і керує мементо.

TextEditor - це зберігач, який представляє текстовий редактор. 
Він має методи для збереження та відновлення стану текстового документа.

У прикладі використання ми створюємо текстовий редактор, 
встановлюємо текст, зберігаємо стан за допомогою мементо, 
змінюємо текст, зберігаємо новий стан, 
а потім відновлюємо попередній стан з мементо. 
Це дозволяє нам зберегти та відновити різні стани текстового документа 
за допомогою патерну "Мементо".
"""

# ====================================================
#  Приклад використання патерну "Мементо" (Memento)
#  в контексті збереження та відновлення стану гри
#  в крестики-нулики
# ====================================================

# Клас Мементо
class Memento:
    def __init__(self, board):
        self.board = board

    def get_board(self):
        return self.board


# Клас Опікун (Caretaker)
class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


# Клас Гри в крестики-нулики (Originator)
class TicTacToeGame:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, player, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
        else:
            print("Invalid move!")

    def display_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("---------")
        print('\n\n')

    def create_memento(self):
        return Memento([row[:] for row in self.board])

    def restore_from_memento(self, memento):
        self.board = [row[:] for row in memento.get_board()]


# Приклад використання
if __name__ == "__main__":
    caretaker = Caretaker()
    game = TicTacToeGame()

    game.make_move('X', 0, 0)
    game.make_move('O', 1, 1)
    game.make_move('X', 1, 0)
    game.make_move('O', 2, 2)

    print('Current state:')
    game.display_board()

    # Зберегти поточний стан гри
    caretaker.add_memento(game.create_memento())

    print('New step and state:')
    game.make_move('X', 2, 0)
    game.make_move('O', 0, 2)

    # Зберегти поточний стан гри
    caretaker.add_memento(game.create_memento())

    game.display_board()

    # Відновити попередній стан гри
    game.restore_from_memento(caretaker.get_memento(0))

    print("Restored state:")
    game.display_board()

    game.restore_from_memento(caretaker.get_memento(1))

    print("Restored state:")
    game.display_board()

# """
# У цьому прикладі ми маємо класи Memento, Caretaker і TicTacToeGame.
# TicTacToeGame представляє гру в крестики-нулики
# і має методи для здійснення ходів,
# відображення стану гри та створення/відновлення мементо.
# Ми можемо зберігати стан гри, робити ходи,
# а потім відновлювати попередній стан за допомогою мементо.
#
# У прикладі використання ми створюємо гру, робимо кілька ходів,
# зберігаємо стан гри в мементо, робимо додаткові ходи,
# а потім відновлюємо попередній стан гри.
# Це дозволяє гравцям зберігати та відновлювати стан гри
# за допомогою патерну "Мементо".
# """