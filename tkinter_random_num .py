from tkinter import *
from tkinter import ttk
import random
window = Tk()
window.geometry("400x400+300+150")
window.title("Nacho's Guessing Game")
x = random.randint(1,100)

def enter():
    guess = int(ent_input.get())
    print(X)
    if guess == x:
        lbl_result.config(text="You guess correctly")
    elif guess > x:
        lbl_result.config(text="You are too high")
    elif guess < x:
        lbl_result.config(text="You are too low")
    else:
        lbl_result.config(text="You are wrong.")

lbl_inst = ttk.Label(window, text = "Guess the number in Nacho's mind ;) (between 1 and 100)")
lbl_inst.config(font = ("Times", "26"))
lbl_inst.pack()
ent_input = ttk.Entry (window, width=5)
ent_input.pack()
btn_Enter = ttk.Button(window,text="Click after guess", command=enter)
btn_Enter.pack()
lbl_result = ttk.Label(window,text="Result will be displayed")
lbl_result.config(font=("Times", "26"))
lbl_result.pack()

window.mainloop()
