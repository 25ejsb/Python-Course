from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"

window = Tk()
window.title("Very Cool Timer")
window.minsize(500, 500)
window.maxsize(500, 500)
window.config(padx=100, pady=50, bg=YELLOW)

breaks = 0
minutes = 0
count = 0
stopTimer = False
checkmarkText = ""

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

photo = PhotoImage(file="Day28/tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=("Arial", 20, "bold"))
canvas.grid(column=1, row=1)

timerText = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
timerText.grid(column=1, row=0)

def addCheckmark():
    global checkmarkText
    checkmarkText = checkmarkText + CHECKMARK
    checkmarks.config(text=checkmarkText)

def count_down(m, c):
    global minutes, count
    minutes = m
    count = c
    timerText.config(text="Timer")
    if count < 10:
        if stopTimer == False:
            canvas.itemconfig(timer_text, text=str(minutes) + ":0" + str(count))
    else:
        if stopTimer == False:
            canvas.itemconfig(timer_text, text=str(minutes) + ":" + str(count))
    if count <= 0 and minutes <= 0:
        global breaks
        breaks += 1
        window.attributes('-topmost', 1)
        if breaks >= 4:
            breaks = 0
            break_time(20, 0)
        else:
            break_time(5, 0)
        return 
    elif count <= 0:
        count = 59
        if stopTimer != True:
            window.after(1000, count_down, minutes-1, count)
    elif count > 0:
        if stopTimer != True:
            window.after(1000, count_down, minutes, count-1)

def break_time(m, c):
    global minutes, count
    minutes = m
    count = c
    timerText.config(text="Break")
    if count < 10:
        if stopTimer == False:
            canvas.itemconfig(timer_text, text=str(minutes) + ":0" + str(count))
    else:
        if stopTimer == False:
            canvas.itemconfig(timer_text, text=str(minutes) + ":" + str(count))
    if count <= 0 and minutes <= 0:
        count_down(25, 0)
        window.attributes('-topmost', 1)
        addCheckmark()
        return
    elif count <= 0:
        count = 59
        if stopTimer != True:
            window.after(1000, break_time, minutes-1, count)
    elif count > 0:
        if stopTimer != True:
            window.after(1000, break_time, minutes, count-1)

def start_timer():
    global stopTimer
    stopTimer = False
    count_down(25, 0)

def resetTimer():
    global minutes, count, stopTimer, breaks, checkmarkText
    breaks = 0
    minutes = 0
    count = 0
    stopTimer = True
    checkmarkText = ""
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

reset = Button(text="Reset", font=("Arial", 10), command=resetTimer)
reset.grid(column=2, row=2)

start = Button(text="Start", font=("Arial", 10), command=start_timer)
start.grid(column=0, row=2)

checkmarks = Label(text="", font=("Arial", 15), bg=YELLOW, highlightthickness=0, fg=GREEN)
checkmarks.grid(column=1, row=2)

window.mainloop()