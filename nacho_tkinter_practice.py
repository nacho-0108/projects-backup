from tkinter import *
import tkinter as tk

q = 0
s = -1
count = 0
correct = 0
incorrect = 0

question = ["What is 1+2?","What is 9/3?","What is 5+8?","What is 13*2?"]

answer = ["3","3","13","26"]
answer_cap = ["3","3","13","26"]

root = Tk()

name = tk.Label(root,text = "LIttle Math Game")
name.pack()

label = tk.Label(root,text = question[0])
label.pack()  

entry = tk.Entry(root)
entry.pack()



def out():
    global q,correct,incorrect,s,count
    count = count + 1
    ans = entry.get()
    print (ans)
    print (question[q])
    print (answer[q])
    if count < 4:
          if answer[q] or answer_cap[q] == ans :
              q = q + 1
              entry.delete(0, END)
              correct = correct + 1
              label.config(text = question[q])
          else:
              q = q + 1
              entry.delete(0, END)
              incorrect = incorrect + 1
              label.config(text = question[q])
    else:
        entry.delete(0, END)
        label.config(text = "Correct: "+str(correct) + " Incorrect:   "+str(incorrect))


def stop():
    global q,correct,incorrect
    q = 0
    correct = 0
    incorrect = 0
    entry.delete(0, END)
    label.config(text = question[0])

button = tk.Button(root,text = "Submit",command = out)
button.pack()

button_two = tk.Button(root,text = "Restart",command = stop)
button_two.pack()


root.mainloop()   
