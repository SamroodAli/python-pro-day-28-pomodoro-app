"""Pomodoro app mail file"""
# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import pygame
import math
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
reps = 0
# to track the window after API, so we can cancel it
timer = None
# init pyfame module for sound
pygame.init()

# ---------------------------- TIMER RESET ------------------------------- #
# Button  event listeners
def reset_event():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
# Button  event listeners
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_term_break = LONG_BREAK_MIN * 60

#   If it is the 8th rep [every 8th rep]:
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_term_break)
#   If it's the 2nd, 4th, 6th rep [even numbers]:
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
#   If it's the 1st, 3rd, 5th, 7th rep:
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# -------------------====----- COUNTDOWN MECHANISM --------------------------- #
# using recursion to decrement count
def count_down(count):
    count_min = math.floor(count/60)
    # seconds = remainder after division by 60
    count_sec = count % 60
    # code for changing single zero to double zero
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # access canvas.config
    # pass in the variable to which canvas.create_text() is assigned
    # change text to new string data, here count
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # code for sound
        pygame.mixer.music.load("bell-ring-01.wav")
        pygame.mixer.music.play()
        # code for checkmarks
        checkmarks = ""
        # 1 work and 1 break [ 2 reps  ] = 1 completed work session
        completed_work_sessions = math.floor(reps/2)
        for _ in range(completed_work_sessions):
            checkmarks += "✔"
        checkmarks_label.config(text=checkmarks)

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
reset_button = Button(text="Reset", command=reset_event, bg="white", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Label Checkmarks
checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=CHECKMARKS_LABEL_FONT)
checkmarks_label.grid(column=1, row=3)

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

# ---------------------------- Tkinter window on loop ------------------------------- #
window.mainloop()
