import random
import turtle
t = turtle.Turtle()
t.speed('fastest')
col = [0,0,0,0,0,0,0,0,0,0] #array of integers
colours = ['red','yellow','purple','cyan','dark green','orange','black','green','purple','light blue']
startx = -150 # x and y co-ords i.e. where to draw chart
starty = -150
loop = 1000 #set the loop to 1000
bar_width = 50
ran_data = []
for i in range(loop):
    n = random.randint(0,200) #create a random integer 0 - 100
    n2 = random.randint(0,200)
    n = (n + n2)/2 #calculate the mean of the two random numbers
    ran_data.append(n) #add the number to the array
for i in range(loop):
    if ran_data[i] >= 0 and ran_data[i] <= 20:
        col[0] += 1
    elif ran_data[i] > 20 and ran_data[i] <= 40:
        col[1] += 1
    elif ran_data[i] > 40 and ran_data[i] <= 60:
        col[2] += 1
    elif ran_data[i] > 60 and ran_data[i] <= 80:
        col[3] += 1
    elif ran_data[i] > 80 and ran_data[i] <= 100:
        col[4] += 1
    elif ran_data[i] > 100 and ran_data[i] <= 120:
        col[5] += 1
    elif ran_data[i] > 120 and ran_data[i] <= 140:
        col[6] += 1
    elif ran_data[i] > 140 and ran_data[i] <= 160:
        col[7] += 1
    elif ran_data[i] > 160 and ran_data[i] <= 180:
        col[8] += 1
    elif ran_data[i] > 180 and ran_data[i] <= 200:
        col[9] += 1 
t.up()
t.goto(startx,starty)
t.down()
t.forward(330)
t.backward(330)
t.left(90)
t.forward(330)
t.backward(330)
t.right(90)
t.up()
t.goto(startx,starty) #position the start point
t.down()
for i in range(10):
    t.fillcolor(colours[i])
    t.begin_fill()
    t.forward(bar_width)
    t.backward(bar_width)
    t.left(90)
    t.forward(col[i])
    t.up()
    t.forward(5)
    t.right(90)
    t.forward(10)
    t.write(col[i])
    t.backward(10)
    t.left(90)
    t.backward(5)
    t.down()
    #-----------------#
    t.right(90)
    t.forward(bar_width)
    t.right(90)
    t.forward(col[i])
    t.end_fill()
    t.left(90)

    
