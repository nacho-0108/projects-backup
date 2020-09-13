#Created 2017.08.03
#---------------subroutines-----------
def correlation():
    global size #use 6 and don't create a new local variable
    person1[0] = int(ent_cinema1.get()) #get contents of the label
    person2[0] = int(ent_cinema2.get())
    person1[1] = int(ent_dinner1.get())
    person2[1] = int(ent_dinner2.get())
    person1[2] = int(ent_sport1.get())
    person2[2] = int(ent_sport2.get())
    #----------------------------------
    sigma = 0
    diff = [0 for i in range(size)]
    for i in range(0, size):
        diff[i] = person1[i] - person2[i]
        diff[i] = diff[i] ** 2
        sigma += diff[i]
    total = 1 - ((size * sigma) / (size * ((size**2) - 1)))
    total = total * 100
    #-----------------------------------
    if total >= 90:
        lbl_result.config(text = "The perfect match: " + str(total))
    elif total >= 70:
        lbl_result.config(text = "You are compatible: " + str(total))
    elif total >= 50:
        lbl_result.config(text = "A little different in some ways: " + str(total))
    elif total >= -50:
        lbl_result.config(text = "Not a good match: " + str(total))
    else:
        lbl_result.config(text = "You have found your mortal enemy: " + str(total))    

#------main program-----------#    
import time
from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.title("Friendship quiz algorithm ;)")
root.geometry("300x200+50+150")

size = 3 #number of items
person1 = [0 for i in range(size)] #array
person2 = [0 for i in range(size)]
#---------------------------------
lbl_heading = ttk.Label(root, text = "Please rank your choices (1-3)")
lbl_heading.grid(row=0, column=1, columnspan=3)
#---------------------------------
lbl_cinema = ttk.Label(root, text = "Cinema")
lbl_cinema.grid(row=1, column = 1)
ent_cinema1 = ttk.Entry(root,width=5) #cinema labels
ent_cinema1.grid(row=1, column=2)
ent_cinema2 = ttk.Entry(root,width=5)
ent_cinema2.grid(row=1, column = 3)
#---------------------------------
lbl_sport = ttk.Label(root, text = "Dinner")
lbl_sport.grid(row=2, column = 1)
ent_dinner1 = ttk.Entry(root,width=5) #cinema labels
ent_dinner1.grid(row=2, column = 2)
ent_dinner2 = ttk.Entry(root,width=5)
ent_dinner2.grid(row=2, column = 3)
#---------------------------------
lbl_sport = ttk.Label(root, text = "Sport")
lbl_sport.grid(row=3, column = 1)
ent_sport1 = ttk.Entry(root,width=5) #cinema labels
ent_sport1.grid(row=3, column =2)
ent_sport2 = ttk.Entry(root,width=5)
ent_sport2.grid(row=3,column=3)
#---------------------------------
btn_submit = ttk.Button(root, text = "Submit", command = correlation)
btn_submit.grid(row = 4, column = 1, columnspan=3)
lbl_result = ttk.Label(root, text = "")
lbl_result.grid(row=5, column = 1,columnspan=3)
