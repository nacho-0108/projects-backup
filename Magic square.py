size = 3 # grid size
total = size**2 # 9 i.e. the last number on a 3 x 3 grid
magic = True #boolean
magic_tot = 0 #initialise the total
grid = [[0 for x in range(size)] for y in range(size)]

def init2():
    count = 1
    global size
    global total
    y = int((size) / 2)
    x = 0
    grid[x][y] = count #[0][1]
    for n in range(total):
        oldx = x #variables for if a cell is taken
        oldy = y
        if x == 0: #if on the top row
            x = size-1 #bottom row
        else:
            x = x - 1 #move up one row
        #end if
        if y == size-1: #if on right col
            y = 0 #go to first col
        else:
            y = y + 1 #move to next col
        #end if
        count = count + 1
        if grid[x][y] == 0: #is the cell empty
            grid[x][y] = count
        else: #already taken go below
            if count < total: #grid is full
                x = oldx + 1
                y = oldy
                grid[x][y] = count
            #end if
        #end if
        printGrid()
    #end loop
#end subroutine
def printGrid():
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end=" ")
        print("")
    print("_______")
init2()

#calculate the total for a row, col, diag
for n in range(1,total+1): # loop 1 to 25 and add them all together
    magic_tot +=n
#end loop
magic_tot = magic_tot / size # 
col = [0 for x in range(size)]
#check cols
x = 0
while x < size and magic == True:
    for y in range(size):
        col[x] += grid[y][x]
    #end loop
    if (col[x] != magic_tot):
        magic = False
    #end if
    x += 1
#end loop
row = [0 for x in range(size)]
#check rows
y = 0
while y < size and magic == True:
    for x in range(size):
        row[y] += grid[y][x]
    #end loop
    if (row[y] != magic_tot):
        magic = False
    #end if
    y += 1
#end loop
diag1 = 0
diag2 = 0
#check diagnals
for y in range(size):
    diag1 += grid[y][y]
#end loop
for x in range(size):
    diag2 += grid[size-1-x][x]
#end loop
if diag1 != magic_tot or diag2 != magic_tot: #check diagnals
    magic == False
#end if
printGrid()
if (magic == True): #if magic remains True then print
    print("You've got the magic")
    print(col, row, diag1, diag2)
else:
    print("Not so magical")
#end if

