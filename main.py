from random import randint
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

def start():
    # Циклы для создания списков
    global easy_board, board, row, game, label_win
    label_win["text"] = ""
    board = []
    row = []
    game = True

    for i in range(3):
        for j in range(3):
            row.append(TicButton(j, i))
        board.append(row)
        row = []

    easy_board = []
    for i in range(3):
        for j in range(3):
            row.append(board[i][j])
        easy_board.append(row)
        row = []

def versions():
    try:
        open("readme.txt", "r")
    except FileNotFoundError:
        messagebox.showerror(title="Ой", message="Похоже, вайл с версиями где то потерялся")
    else:
        os.startfile("readme.txt")


window = tk.Tk()
window.geometry("900x600")
window.title("Крестики-нолики")

menu = tk.Menu(window)

menu_file = tk.Menu(menu, tearoff=0)
menu_file.add_command(label="История изменений", command=versions)
menu_file.add_command(label="Выйти", command=sys.exit)

menu.add_cascade(label="Основное", menu=menu_file)
window.config(menu=menu)

frame = ttk.Frame(window, width=600, height=600)
frame.grid(row=2, column=2, sticky="nsew")

style_but = ttk.Style()
style_but.configure('my.TButton', font=('Helvetica', 20))

style_win = ttk.Style()
style_win.configure('my.TLabel', font=('Helvetica', 20))

label_win = ttk.Label(frame, text="", style="my.TLabel")
label_win.grid(row=3, column=4)

easy_board = []
board = []
row = []

game = True

button_reset = ttk.Button(frame, text="Перезапустить", style="my.TButton", command=start)
button_reset.grid(row=4, column=4, ipadx=10, ipady=10, sticky="nesw")

class TicButton():
    def __init__(self, corx = int, cory = int):
        self.x = corx
        self.y = cory
        self.button = ttk.Button(frame, text=" ", style="my.TButton", command=self.button_click)
        self.button.grid(row=self.y+2, column=self.x+1, ipady=50, ipadx=10, sticky="nsew")

    # Событие нажатия на кнопку
    def button_click(self):
        global game
        if game:
            if not self.button["text"] in ("X","0"):
                # Добавить выбор знака
                self.button["text"] = "X"
                self.win_test()
                self.computer()

    # Компьютер ходит
    def computer(self):
        global board, game
        if game:
            compx = randint(0,2)
            compy = randint(0,2)
            if not board[compy][compx].button["text"] in ("X","0"):
                board[compy][compx].button["text"] = "0"
                self.win_test()
            else:
                self.computer()

# Проверка (не трогать)
    def win_test(self):
        global board, easy_board, game
        for i in range(3):
            for j in range(3):
                easy_board[j][i] = board[j][i].button["text"]


        # hor
        for row in easy_board:
            if row.count("X") == 3:
                self.win_set("X")

            elif row.count("0") == 3:
                game = False
                self.win_set("0")

        # ver
        h = []
        for i in range(3):
            for row in easy_board:
                h.append(row[i])
            if h.count("X") == 3:
                self.win_set("X")

            elif h.count("0") == 3:
                game = False
                self.win_set("0")

            else:
                h=[]

        # diag
        for xo in ("X","0"):
            condition1 = easy_board[0][0] == easy_board[1][1] == easy_board[2][2] and easy_board[0][0] == xo
            condition2 = easy_board[2][0] == easy_board[1][1] == easy_board[0][2] and easy_board[2][0] == xo
            if condition1 or condition2:
                self.win_set(xo)
    def win_set(self, win):
        global game, label_win
        game = False
        label_win['text'] = f"{win} win!"


# создание пустого игрового поля



start()

window.mainloop()