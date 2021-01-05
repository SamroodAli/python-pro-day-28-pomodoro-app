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
TIMER_LABEL_FONT = ("Georgia", 50, "italic")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARKS_LABEL_FONT = ("Courier", 20, "normal")


# ---------------------------- TIMER RESET ------------------------------- #
# Button  event listeners
def button_reset_on_event():
    print("Do something")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


# Button  event listeners
def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# using recursion to decrement count
def count_down(count):
    # access canvas.config
    # pass in the variable to which canvas.create_text() is assigned
    # change text to new string data, here count
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
# tkinter window
window = Tk()
window.title("Pomodoro")

# window resizing
window.config(padx=100, pady=50, bg=YELLOW)

# ---------------------------- Widgets ------------------------------- #

# Label
timer_label = Label(text="Timer", font=TIMER_LABEL_FONT, fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", command=start_timer, bg="white", highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=button_reset_on_event(), bg="white", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Label Checkmarks
checkmarks = Label(text="✔", fg=GREEN, bg=YELLOW, font=CHECKMARKS_LABEL_FONT)
checkmarks.grid(column=1, row=3)

# highlightthickness is  to remove the borders around the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# canvas image requires a PhotoImage instance
TOMATO_IMG = PhotoImage(file="tomato.png")
# for center image, give x and y half of width and height, x = 101 not 100 as the image was due highlightthicknessm,
# changed back to 100 after highlightthickness = 0
canvas.create_image(100, 112, image=TOMATO_IMG)

# laying text on top, x and y placements 103,130, fill = font-color, font-tuple
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=TIMER_FONT)
canvas.grid(column=1, row=1)

# starting countdown
window.mainloop()
