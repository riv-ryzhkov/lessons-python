from tkinter import *


def button_clicked1():
    print("Клик синей кнопки!")


def button_clicked2():
    print("Клик красной кнопки!")

root = Tk()

canvas = Canvas(root, width=300, height=100, bd=0, highlightthickness=100)
canvas.pack()
# кнопка по умолчанию
button1 = Button(root, bg="blue", text=" Я синяя кнопка! Кликни меня! ", command=button_clicked1)
button1.pack()
# кнопка с указанием родительского виджета и несколькими аргументами
button2 = Button(root, bg="red", text=" Я красная кнопка! Кликни меня! ", command=button_clicked2)
button2.pack()
root.mainloop()

# from tkinter import *
# # import tkinter
# import time
# import random
# #
# #
# # window = Tk()
# # greeting = tk.Label(text="Привет, Tkinter!")
# # greeting.pack()
# #
# tk = Tk()
# tk.title('Arkanoid')
# tk.resizable(0, 0)
# tk.wm_attributes('-topmost', 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()
# # tk.mainloop()
#
#
# class Ball:
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
#         self.canvas.move(self.id, 250, 150)
#         start = list(range(-3, 4))
#         start.remove(0)
#         random.shuffle(start)
#         self.x = start[0]
#         self.y = start[1]
#         self.canvas_height = self.canvas.winfo_height()
#         self.canvas_wigth = self.canvas.winfo_width()
#
#
#
#     def draw(self):
#         self.canvas.move(self.id, self.x, self.y)
#         pos = self.canvas.coords(self.id)
#         # print(pos)
#         #         x1      y1     x2      y2
#         # print(pos[0], pos[1], pos[2], pos[3])
#         if pos[1] <= 0 or pos[3] >= self.canvas_height:
#             self.y *= -1
#             # self.y = 1
#
#         # if pos[3] >= self.canvas_height:
#         #     self.y = -1
#
#         if pos[0] <= 0 or pos[2] >= self.canvas_wigth:
#             self.x *= -1
#         # if pos[0] <= 0:
#         #     self.x = 1
#         # if pos[2] >= self.canvas_wigth:
#         #     self.x = -1
#
# ball = Ball(canvas, "red")
# while True:
#     ball.draw()
#     tk.update_idletasks()
#     tk.update()
#     time.sleep(0.005)

