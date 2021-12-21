import tkinter as tk
root = tk.Tk()
root.geometry("1000x1000")
surface = tk.Frame()
surface.master.title("G14 Master Eat")
canvas = tk.Canvas(surface)
background = tk.PhotoImage(file="C:\\Users\\student\\Desktop\\GameProject-G14\\images\\bggm.png")
eaterImage = tk.PhotoImage(file="C:\\Users\\student\\Desktop\\GameProject-G14\\images\\eater.png")
wallOutside = tk.PhotoImage(file="C:\\Users\\student\\Desktop\\GameProject-G14\\images\\wallaround.png")
wallInside = tk.PhotoImage(file="C:\\Users\\student\\Desktop\\GameProject-G14\\images\\wall.png")

array2DToMakeGrid = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,3,3,3,0,0,0,1],
    [1,3,3,3,0,0,0,0,0,3,0,1],
    [1,0,0,0,3,3,3,3,0,3,0,1],
    [1,0,0,0,3,0,3,0,0,3,0,1],
    [1,0,3,3,3,0,3,0,3,0,0,1],
    [1,0,0,0,0,0,0,0,3,0,0,1],
    [1,3,3,3,3,0,3,0,3,0,0,1],
    [1,0,0,0,0,0,3,0,3,3,3,1],
    [1,3,3,3,3,3,3,0,0,0,0,1],
    [1,2,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]]

canvas.create_image(0,0,image=background,anchor="nw")
# Make grid and put character (eater)
def makeGrid():
    y1 = 30
    y2 = 70
    for row in array2DToMakeGrid:
        x1 = 250
        x2 = 290
        for col in row:
            if col == 2:
                canvas.create_image(x1+20,y1+20,image=eaterImage,tags="toMove")
            elif col == 1:
                canvas.create_image(x1+20,y1+20,image=wallOutside,tags="wall")
            elif col == 3:
                canvas.create_image(x1+20,y1+20,image=wallInside,tags="wall")
            else:
                canvas.create_rectangle(x1,y1,x2,y2)     
            x1=x2
            x2+=40
        y1 = y2
        y2 += 40


def positionEaterOnRow(array2DToMakeGrid):
    rowIndex = 0
    while rowIndex < len(array2DToMakeGrid):
        if 2 in array2DToMakeGrid[rowIndex]:
            return rowIndex
    rowIndex += 1


def positionEaterOnCol(array2DToMakeGrid):
    rowIndex = 0
    while rowIndex < len(array2DToMakeGrid):
        if 2 in array2DToMakeGrid[rowIndex]:
            colIndex = 0
            while colIndex < len(array2DToMakeGrid[rowIndex]):
                if array2DToMakeGrid[rowIndex][colIndex] == 2:
                    return colIndex
                colIndex += 1
        rowIndex+=1

def moveToRight(event):
    indexOfRow=positionEaterOnRow(array2DToMakeGrid)
    indexOfCol=positionEaterOnCol(array2DToMakeGrid)
    if indexOfCol+1<len(array2DToMakeGrid[0]):
        array2DToMakeGrid[indexOfRow][indexOfCol]=0
        array2DToMakeGrid[indexOfRow][indexOfCol+1]=2
    makeGrid()
makeGrid()

root.bind("<Right>",moveToRight)                
        
canvas.pack(expand=True, fill= "both")
surface.pack(expand=True, fill = "both")
surface.mainloop()
