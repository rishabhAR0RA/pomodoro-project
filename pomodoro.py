from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer = None


def reset_timer():
    """
    It resets the reps counter, cancels the timer, resets the timer text, resets the timer label, and
    resets the check label
    """
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    timer_label.config(text="Timer", fg="green")
    check_label.config(text="")


def start_timer():
    """
    If the number of reps is divisible by 8, then it's a long break, if it's divisible by 2, then it's a
    short break, otherwise it's a work period
    """
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg="red")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg="pink")
        count_down(short_break_sec)
    else:
        timer_label.config(text="Timer", fg="green")
        count_down(work_sec)


def count_down(count):
    """
    `count_down` takes a number of seconds as an argument and displays it in the format `mm:ss` on the
    canvas

    Args:
      count: the number of seconds to count down from
    """
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = "".join("✓" for _ in range(reps // 2))
        check_label.config(text=mark)


window = Tk()
window.title("Countdown Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", width=10, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", width=10, highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 15, "normal"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
