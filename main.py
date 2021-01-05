"""Pomodoro app mail file"""
# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window resizing
window.config(padx=100, pady=50)
# Canvas Widget
canvas = Canvas(width=200, height=224)
# canvas image requires a PhotoImage instance
tomato_img = PhotoImage(file="tomato.png")
# for center image, give x and y half of width and height, x = 101 not 100 as the image was due to some reason
# shifted to the right
canvas.create_image(101, 112, image=tomato_img)
canvas.pack()

window.mainloop()
