"""Pomodoro app mail file"""
# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TIMER_FONT = (FONT_NAME, 35, "bold")
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
window.config(padx=100, pady=50, bg=YELLOW)
# highlightthickness is  to remove the borders around the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# canvas image requires a PhotoImage instance
tomato_img = PhotoImage(file="tomato.png")
# for center image, give x and y half of width and height, x = 101 not 100 as the image was due highlightthicknessm,
# changed back to 100 after highlightthickness = 0

canvas.create_image(100, 112, image=tomato_img)
# laying text on top, x and y placements 103,130, fill = font-color, font-tuple
canvas.create_text(100, 130, text="00:00", fill="white", font=TIMER_FONT)
canvas.pack()

window.mainloop()
