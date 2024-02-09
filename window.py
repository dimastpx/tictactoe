from random import randint
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x600")
frame = ttk.Frame(window, width=500, height=500)
frame.grid(sticky="nsew")

style = ttk.Style()
style.configure('my.TButton', font=('Helvetica', 20))

class TicButton():
    def __init__(self, corx = int, cory = int):
        self.x = corx + 1
        self.y = cory + 1
        self.button = ttk.Button(frame, text=" ", style="my.TButton", command=self.button_click)
        self.button.grid(row=self.y, column=self.x, ipady=50, ipadx=10, sticky="nsew")
    def button_click(self):
        if not self.button["text"] in ("X","0"):
            # Добавить выбор знака
            self.button["text"] = "X"


# Цикл для создания списка

board = []
row = []
for i in range(3):
    for j in range(3):
        row.append(TicButton(j, i).y)
    board.append(row)
    row = []

for i in board:
    print(i)


window.mainloop()