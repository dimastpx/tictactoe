from random import randint
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x600")
frame = ttk.Frame(window, width=500, height=500)
frame.grid(sticky="nsew")



for i in range(3):
    for j in range(3):
        button = ttk.Button(frame, text=j)

        button.grid(row=i, column=j, sticky="nsew")


window.mainloop()