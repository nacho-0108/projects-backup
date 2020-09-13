from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("600x400+300+150")
window.title("High Score Table")

def bubbleSort():
    swapped = True
    n= len(myList)
    while swapped == True:
        swapped = False
        n = n-1
        for i in range (0,n):
            if highscores[p]>myList[p+1]:
                temp = myList[p]
                myList[p] = myList[p+1]
                myList[p+1] = temp
                swapped = True

def write():
#   read()
    name = ent_name.get()
    score = ent_score.get()
    arr_hs.append(name+""+score)
    bubbleSort()
    file = open("highscores.txt", "w")
    for item in arr_hs:
        file.write("%s\n" % item)
    display()
    ent_name.delete(0,len(name))
    ent_score.delete(0,len(score))

def read():
    arr_hs.clear()
    file=open("highscores.txt", "r")
    for line in file:
        arr_hs.append(line.strip())
    file.close()
    display()

def display():
    output = "High Scores" + "\n"
    for n in range(len(arr_hs)):
        output+=arr_hs[n] + "\n"
    lbl_result.config(text= output)        

arr_hs = []

lbl_inst = ttk.Label(window, text = "Enter your data to add e.g. Name, Score")
lbl_inst.config(font=("Times", "26"))
lbl_inst.grid(row=0, column =0, columnspan=4)
ent_name = ttk.Entry(window, width = 10)
ent_name.grid(row=1, column = 0)
ent_score = ttk.Entry(window,width = 4)
ent_score.grid(row=1, column =1)
btn_Write= ttk.Button(window,text="Write", command=write)
btn_Write.grid(row=2, column=0)
btn_Read = ttk.Button(window, text="Read", command=read)
btn_Read.grid (row=2, column=1)
lbl_result = ttk.Label(window, font=("Times","18"), text="Top Scores")
lbl_result.grid(row=3, column=0)

window.mainloop()
