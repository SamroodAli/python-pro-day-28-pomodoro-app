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
TIMER_LABEL_FONT = (FONT_NAME, 30, "normal")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# tkinter window
window = Tk()
window.title("Pomodoro")

# window resizing
window.config(padx=100, pady=50, bg=YELLOW)

# ---------------------------- Widgets ------------------------------- #

# Label
label = Label(text="Timer", font=TIMER_LABEL_FONT)
label.grid(column=1, row=0)
# Buttons


# Button  event listeners
def button_start_on_event():
    print("Do something")


# Button  event listeners
def button_reset_on_event():
    print("Do something")


button_start = Button(text="Start", command=button_start_on_event())
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", command=button_reset_on_event())
button_reset.grid(column=2, row=2)

# highlightthickness is  to remove the borders around the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# canvas image requires a PhotoImage instance
TOMATO_IMG = PhotoImage(file="tomato.png")
# for center image, give x and y half of width and height, x = 101 not 100 as the image was due highlightthicknessm,
# changed back to 100 after highlightthickness = 0
canvas.create_image(100, 112, image=TOMATO_IMG)

# laying text on top, x and y placements 103,130, fill = font-color, font-tuple
canvas.create_text(100, 130, text="00:00", fill="white", font=TIMER_FONT)
canvas.grid(column=1, row=1)

window.mainloop()
