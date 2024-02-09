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
        self.x = corx
        self.y = cory
        self.button = ttk.Button(frame, text=" ", style="my.TButton", command=self.button_click)
        self.button.grid(row=self.y, column=self.x, ipady=50, ipadx=10, sticky="nsew")

    # Событие нажатия на кнопку
    def button_click(self):
        if not self.button["text"] in ("X","0"):
            # Добавить выбор знака
            self.button["text"] = "X"
            self.win_test()
            self.computer()

    # Компьютер ходит
    def computer(self):
        global board
        compx = randint(0,2)
        compy = randint(0,2)
        if not board[compy][compx].button["text"] in ("X","0"):
            board[compy][compx].button["text"] = "0"
            self.win_test()
        else:
            self.computer()

# Проверка (не трогать)
    def win_test(self):
        global board, easy_board
        for i in range(3):
            for j in range(3):
                easy_board[j][i] = board[j][i].button["text"]
        print(easy_board)

        # hor
        for row in easy_board:
            if row.count("X") == 3 or row.count("0") == 3:
                exit("Game over")
        # ver
        h = []
        for i in range(3):
            for row in easy_board:
                h.append(row[i])
            if h.count("X") == 3 or h.count("0") == 3:
                exit("Game over")
            else:
                h=[]

        # diag
        condition1 = easy_board[0][0] == easy_board[1][1] == easy_board[2][2] and easy_board[0][0] in ("X", "0")
        condition2 = easy_board[2][0] == easy_board[1][1] == easy_board[0][2] and easy_board[2][0] in ("X", "0")
        if condition1 or condition2:
            exit("Game over")


# Цикл для создания списка

board = []
row = []
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




window.mainloop()