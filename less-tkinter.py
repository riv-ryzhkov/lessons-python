# from tkinter import *
#
# root = Tk()
# root.title("Простой калькулятор")
# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#
#
# def button_click(number):
#     # e.delete(0, END)
#     current = e.get()
#     e.delete(0, END)
#     e.insert(0, str(current) + str(number))
#
#
# def button_clear():
#     e.delete(0, END)
#
#
# def button_add():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "addition"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# def button_equal():
#     second_number = e.get()
#     e.delete(0, END)
#
#     if math == "addition":
#         e.insert(0, f_num + int(second_number))
#     if math == "subtraction":
#         e.insert(0, f_num - int(second_number))
#     if math == "multiplication":
#         e.insert(0, f_num * int(second_number))
#     if math == "division":
#         e.insert(0, f_num / int(second_number))
#
#
# def button_subtract():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "subtraction"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# def button_multiply():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "multiplication"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# def button_divide():
#     first_number = e.get()
#     global f_num
#     global math
#     math = "division"
#     f_num = int(first_number)
#     e.delete(0, END)
#
#
# # Определяем кнопки
# button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
# button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
# button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
# button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
# button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
# button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
# button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
# button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
# button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
# button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
# button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
# button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
# button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
# button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
# button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
# # Располагаем кнопки на экране
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)
# button_0.grid(row=4, column=0)
# button_clear.grid(row=4, column=1, columnspan=2)
# button_add.grid(row=5, column=0)
# button_equal.grid(row=5, column=1, columnspan=2)
# button_subtract.grid(row=6, column=0)
# button_multiply.grid(row=6, column=1)
# button_divide.grid(row=6, column=2)
# root.mainloop()


# ========================================================================



# import tkinter as tk
#
# window = tk.Tk()
#
# label = tk.Label(
#     text="Привет, Tkinter!",
#     fg="white",
#     bg="black",
#     width=20,
#     height=20
# )
#
# label.pack()
# window.mainloop()


# from tkinter import *
# import time
#
#
# def tick():
#     label.after(200, tick)
#     label['text'] = time.strftime('%H:%M:%S')
# root = Tk()
# label = Label(font='sans 40')
# label.pack()
# label.after_idle(tick)
# root.mainloop()


# from tkinter import *
# root = Tk()
# frame1 = Frame(root, bg='green', bd=5)
# frame2 = Frame(root, bg='red', bd=5)
# button1 = Button(frame1, text='Первая кнопка')
# button2 = Button(frame2, text='Вторая кнопка')
# frame1.pack()
# frame2.pack()
# button1.pack()
# button2.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# var1=IntVar()
# var2=IntVar()
# check1=Checkbutton(root,text='1 пункт',variable=var1,onvalue=1,offvalue=0)
# check2=Checkbutton(root,text='2 пункт',variable=var2,onvalue=1,offvalue=0)
# check1.pack()
# check2.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# var=IntVar()
# rbutton1=Radiobutton(root,text='1',variable=var,value=1)
# rbutton2=Radiobutton(root,text='2',variable=var,value=2)
# rbutton3=Radiobutton(root,text='3',variable=var,value=3)
# rbutton1.pack()
# rbutton2.pack()
# rbutton3.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# def getV(root):
#     a = scale1.get()
#     print("Значение", a)
#
# scale1 = Scale(root,orient=HORIZONTAL,length=300,from_=50,to=80,
#                tickinterval=5, resolution=1)
# button1 = Button(root, text="Получить значение")
# scale1.pack()
# button1.pack()
# button1.bind("<Button-1>", getV)
# root.mainloop()



# from tkinter import *
# root = Tk()
# text = Text(root, height=3, width=60)
# text.pack(side='left')
# scrollbar = Scrollbar(root)
# scrollbar.pack(side='left')
# # первая привязка
# scrollbar['command'] = text.yview
# # вторая привязка
# text['yscrollcommand'] = scrollbar.set
# root.mainloop()


# from tkinter import *
# root=Tk()
# button1 = Button(text="1")
# button2 = Button(text="2")
# button3 = Button(text="3")
# button4 = Button(text="4")
# button5 = Button(text="5")
# button1.pack(side='left')
# button2.pack(side='top')
# button3.pack(side='left')
# button4.pack(side='bottom')
# button5.pack(side='right')
#
# root.mainloop()


# from tkinter import *
# root=Tk()
# text = Text(wrap=NONE)
# vscrollbar = Scrollbar(orient='vert', command=text.yview)
# text['yscrollcommand'] = vscrollbar.set
# hscrollbar = Scrollbar(orient='hor', command=text.xview)
# text['xscrollcommand'] = hscrollbar.set
# # размещаем виджеты
# text.grid(row=0, column=0, sticky='nsew')
# vscrollbar.grid(row=0, column=1, sticky='ns')
# hscrollbar.grid(row=1, column=0, sticky='ew')
# # конфигурируем упаковщик, чтобы текстовый виджет расширялся
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)
# root.mainloop()


# from tkinter import *
# root=Tk()
# def leftclick(event):
#     print('Вы нажали левую кнопку мыши')
# def rightclick(event):
#     print('Вы нажали правую кнопку мыши')
# button1=Button(root, text='Нажми')
# button1.pack()
# button1.bind('<Button-1>', leftclick)
# button1.bind('<Button-3>', rightclick)
# root.mainloop()