import tkinter as tk
root = tk.Tk()
#====================  Make Window  ==========================
root.geometry("1000x1000")
surface = tk.Frame()
surface.master.title("Ladies Monkey")
canvas = tk.Canvas(surface)
#====================  Supporter   ===========================
import random
import winsound

#====================  All Pictures==========================
win = tk.PhotoImage(file="images\\thewin.png")
lost = tk.PhotoImage(file="images\\loser.png")
background =tk.PhotoImage(file="images\\bg5.png")
eaterImage = tk.PhotoImage(file="images\\eater2.png")
wallOutside = tk.PhotoImage(file="images\\wallaround.png")
wallInside = tk.PhotoImage(file="images\\wall.png")
fruit0=tk.PhotoImage(file="images\\c1.png")
fruit1=tk.PhotoImage(file="images\\fr2.png")
fruit2=tk.PhotoImage(file="images\\fr3.png")
fruit3=tk.PhotoImage(file="images\\fr4.png")
monster1=tk.PhotoImage(file="images\\m3.png")
monster2=tk.PhotoImage(file="images\\m4.png")
firstBackground = tk.PhotoImage(file="images\\bggm1.png") 
character = tk.PhotoImage(file="images\\character.png")
cAnemy1 = tk.PhotoImage(file="images\\cAnemy1.png")




#==================================  Dictionary store value of each fruit and enemies  ==================

allFruitsAndEnimy = [{'position':4,'score':50,"image":fruit2},{'position':5,'score':100,"image":fruit1},{'position':6,'score':150,"image":fruit0},{'position':7,'score':200,"image":fruit3},
{'position':9,'score':-
400,"image":monster1},{'position':8,'score':-500,"image":monster2}]

array2DToMakeGrid = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,4,5,6,6,3,3,3,4,4,4,5,6,6,0,4,1],
        [1,3,3,3,0,7,7,7,0,3,3,3,3,3,8,4,1],
        [1,5,4,6,3,3,3,3,0,3,5,5,5,5,0,4,1],
        [1,0,8,0,3,7,3,7,0,3,5,3,3,4,3,3,1],
        [1,4,3,3,3,0,3,7,3,4,4,3,8,0,0,6,1],
        [1,4,5,5,6,8,0,7,3,6,3,3,4,5,3,6,1],
        [1,3,3,3,3,0,3,7,3,5,6,3,4,3,3,6,1],
        [1,4,4,4,4,0,3,0,3,3,3,3,5,5,3,6,1],
        [1,3,3,3,3,3,3,0,7,7,7,3,3,3,3,6,1],
        [1,2,4,5,6,5,4,8,6,6,6,3,5,5,5,5,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



#=====================  Variable  ================
Score= 0
won=False
lose=False
# lifeUser=4

#===========================  Score of monkey eat  =====================
Score= 0
def positionscore():
    canvas.create_text(500,30,text=Score,fill="white",font="40")

#==========================   Grids with fruits and enemies  ============
def makeGrid():
    global Score,lifeUser
    canvas.delete("all") 
    canvas.create_image(0,0,image=background,anchor="nw")
    y1 = 40
    y2 = 80
    for row in array2DToMakeGrid:
        x1 = 80
        x2 = 120
        for col in row:
            if col == 2:
                canvas.create_image(x1+20,y1+20,image=eaterImage,tags="toMove")
            elif col == 1:
                canvas.create_image(x1+20,y1+20,image=wallOutside,tags="outsideWall")
            elif col == 3:
                canvas.create_image(x1+20,y1+20,image=wallInside,tags="insideWall")
                winsound.PlaySound("sounds\\monkeylaught.wav",winsound.SND_FILENAME)
            for fruit in allFruitsAndEnimy:
                if col == fruit['position']:
                    canvas.create_image(x1+20,y1+20,image=fruit["image"],tags="wall")        
            x1=x2
            x2+=40
        y1 = y2
        y2 += 40
    # for i in range(lifeUser):
    #     canvas.create_image(Positionofuser,15,images=heart,tags="heart")
    #     Positionofuser -= 50
    canvas.create_text(900,60,text="POINTS: "+str(Score),font="Times 15 bold",fill="white")
    canvas.create_text(40,60,text="EXIT",font="Time 15 bold",fill="#FFFFFF",tags="exit")
makeGrid()
#=============================  The grids of the three levels, such as easy, medium and difficult  ===============
#====================  Easy ===========
def easy(event):
    global array2DToMakeGrid
    array2DToMakeGrid = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,4,5,6,6,3,3,3,4,4,4,5,6,6,0,4,1],
        [1,3,3,3,0,7,7,7,0,3,3,3,3,3,8,4,1],
        [1,5,4,6,3,3,3,3,0,3,5,5,5,5,0,4,1],
        [1,0,8,0,3,7,3,7,0,3,5,3,3,4,3,3,1],
        [1,4,3,3,3,0,3,7,3,4,4,3,8,0,0,6,1],
        [1,4,5,5,6,8,0,7,3,6,3,3,4,5,3,6,1],
        [1,3,3,3,3,0,3,7,3,5,6,3,4,3,3,6,1],
        [1,4,4,4,4,0,3,0,3,3,3,3,5,5,3,6,1],
        [1,3,3,3,3,3,3,0,7,7,7,3,3,3,3,6,1],
        [1,2,4,5,6,5,4,8,6,6,6,3,5,5,5,5,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    makeGrid()

#====================  Medium ===========
def medium(event):
    global array2DToMakeGrid
    array2DToMakeGrid = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,3,5,4,6,3,3,6,5,4,4,5,6,6,6,3,1],
        [1,3,5,3,4,5,5,7,3,3,3,3,3,3,8,4,1],
        [1,5,4,3,5,3,3,3,8,3,5,5,5,5,0,4,1],
        [1,0,8,3,7,5,3,7,0,3,5,3,3,4,3,3,1],
        [1,4,3,3,3,6,3,7,3,4,4,3,8,7,7,6,1],
        [1,4,5,3,4,8,3,7,3,6,3,3,0,5,3,6,1],
        [1,3,3,3,3,0,3,7,3,5,6,3,4,3,3,6,1],
        [1,4,4,4,4,5,3,7,3,3,3,3,5,5,3,6,1],
        [1,4,3,3,3,3,3,0,3,7,7,3,3,3,3,6,1],
        [1,2,4,5,6,5,4,8,6,6,6,3,5,5,5,5,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    makeGrid()

#====================  Difficult ===========
def difficult(event):
    global array2DToMakeGrid
    array2DToMakeGrid = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,3,5,6,6,3,3,3,4,4,4,5,6,6,0,4,3,7,1],
        [1,3,3,3,7,7,7,7,0,3,3,3,3,3,8,4,3,7,1],
        [1,5,4,3,3,3,3,3,8,3,5,5,5,5,4,4,7,7,1],
        [1,0,8,0,3,7,3,7,0,3,5,3,3,4,3,3,3,3,1],
        [1,4,3,3,3,0,3,7,3,4,4,3,8,0,5,6,3,7,1],
        [1,4,5,5,6,8,0,7,3,6,3,3,4,5,3,6,7,5,1],
        [1,3,3,3,3,5,3,7,3,5,6,3,4,3,3,6,3,5,1],
        [1,4,4,4,4,6,3,5,3,3,3,3,5,5,3,6,3,6,1],
        [1,3,4,3,3,3,3,0,7,7,7,3,7,3,3,6,3,4,1],
        [1,2,4,3,6,5,4,8,6,3,3,3,3,5,5,0,3,5,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
    makeGrid()


#=====================  Show when player win =================
def endgame():
    global array2DToMakeGrid
    array2DToMakeGrid=[]
    makeGrid()

def displayresult():
    global Score,won,lose
    # myScore="Score:"+str(Score)
    if lose:
        canvas.delete("all")
        if Score<=5000:
            canvas.create_text(40,60,text="EXIT",font="Time 15 bold",fill="#000000",tags="exit")
            canvas.create_image(500,300,image=lost,anchor="center")
            canvas.create_text(500,50,text="You lost!",font="Time 30 bold",fill="#F6BE00",tags="winner") 
            # winsound.PlaySound("sounds\\gameover.wav",winsound.SND_FILENAME)
        elif Score>=5000:
            canvas.create_text(40,60,text="EXIT",font="Time 15 bold",fill="#000000",tags="exit")
            canvas.create_image(500,300,image=win,anchor="center")
            canvas.create_text(500,50,text="You won!",font="Time 30 bold",fill="#F6BE00",tags="winner")
            # winsound.PlaySound("sounds\\winner.wav",winsound.SND_FILENAME)

# #====================  Funtion  ==================
def positionscore():
    canvas.create_text(500,30,text=Score,fill="white",font="40")
#====================== Position of Monster ================
def moveenimy(array2DToMakeGrid):
    enimey=[]
    for index in range(len(array2DToMakeGrid)):
        for cols in range(len(array2DToMakeGrid[index])):
            if array2DToMakeGrid[index][cols]==8:
                enimey.append([index,cols])
    print(enimey)
    return enimey
def moveingrid(array2DToMakeGrid,r,c):
    move=[]
    if (array2DToMakeGrid[r][c-1]==0):
        move.append("left")
    if (array2DToMakeGrid[r][c+1]==0 ):
        move.append("right")
    if (array2DToMakeGrid[r-1][c]==0):
        move.append("up")
    if (array2DToMakeGrid[r+1][c]==0):
        move.append("down")
    return move

#=============================== Monster can move ==================
def canmove():
    global array2DToMakeGrid,lose,win
    getindexenimy=moveenimy(array2DToMakeGrid)
    print(getindexenimy)
    for enemy in getindexenimy:
        rowindex=enemy[0]
        colindex=enemy[1]
        wheretogo=moveingrid(array2DToMakeGrid,rowindex,colindex)
        if len(wheretogo)>0:
            move=random.choice(wheretogo)
            print(move)
            if move=="left":
                if array2DToMakeGrid[rowindex][colindex-1]==2:
                    lose=True
                elif  array2DToMakeGrid[rowindex][colindex-1]==0 and array2DToMakeGrid[rowindex][colindex-1]!=2:
                    # winsound.PlaySound("sounds\\monkeylaught.wav",winsound.SND_FILENAME)
                    array2DToMakeGrid[rowindex][colindex]=0
                    array2DToMakeGrid[rowindex][colindex-1]=8
            if move=="right":
                if array2DToMakeGrid[rowindex][colindex+1]==2:
                    lose=True
                elif array2DToMakeGrid[rowindex][colindex+1]==0 and array2DToMakeGrid[rowindex][colindex+1]!=2:
                    # winsound.PlaySound("sounds\\monkeylaught.wav",winsound.SND_FILENAME)
                    array2DToMakeGrid[rowindex][colindex]=0
                    array2DToMakeGrid[rowindex][colindex+1]=8
            if move=="up":
                if array2DToMakeGrid[rowindex-1][colindex]==2:
                    lose=True
                elif array2DToMakeGrid[rowindex-1][colindex]==0 and array2DToMakeGrid[rowindex-1][colindex]!=2:
                    # winsound.PlaySound("sounds\\monkeylaught.wav",winsound.SND_FILENAME)
                    array2DToMakeGrid[rowindex][colindex]=0
                    array2DToMakeGrid[rowindex-1][colindex]=8
            if move=="down":
                if array2DToMakeGrid[rowindex+1][colindex]==2:
                    lose=True
                elif array2DToMakeGrid[rowindex+1][colindex]==0 and array2DToMakeGrid[rowindex+1][colindex]!=2:
                    # winsound.PlaySound("sounds\\monkeylaught.wav",winsound.SND_FILENAME)
                    array2DToMakeGrid[rowindex][colindex]=0
                    array2DToMakeGrid[rowindex+1][colindex]=8
    canvas.delete("all") 
    canvas.after(2000,canmove)  
    makeGrid() 
    if lose:
        endgame()
        displayresult()
canvas.after(5000,canmove)
#=========================== Sum each score ============================
def sumscore(allFruitsAndEnimy,indexCol,indexRow):
    global Score
    for fruit in allFruitsAndEnimy:
            if array2DToMakeGrid[indexRow][indexCol+1] == fruit["position"]:
                Score+=fruit["score"]
            if array2DToMakeGrid[indexRow][indexCol-1] == fruit["position"]:
                Score+=fruit["score"]
            if array2DToMakeGrid[indexRow-1][indexCol] == fruit["position"]:
                Score+=fruit["score"]
            if array2DToMakeGrid[indexRow-1][indexCol] == fruit["position"]:
                Score+=fruit["score"]
    return Score

#========================= Player Position ==============================
def finduserposition(array2DToMakeGrid):
    userposition=[]
    for index in range(len(array2DToMakeGrid)):
        for cols in range(len(array2DToMakeGrid[index])):
            if array2DToMakeGrid[index][cols]==2:
                userposition.append([index,cols])
    print(userposition)
    return userposition
#==========================  Find index on row  ==========================
def findRow(grid):
    indexRow = 0
    while indexRow < len(grid):
        if 2 in grid[indexRow]:
            return indexRow
        indexRow += 1
#=========================  Find index on col  ===========================
def findCol(grid):
    indexRow = 0
    while indexRow < len(grid):
        if 2 in grid[indexRow]:
           indexCol = 0
           while indexCol <len(grid[indexRow]):
               if grid[indexRow][indexCol] == 2:
                   return indexCol
               indexCol += 1
        indexRow += 1
#========================  Move player to right ==========================

def moveRight(event):
    global Score,lose,won,array2DToMakeGrid
    if not lose:
        indexCol = findCol(array2DToMakeGrid)
        indexRow = findRow(array2DToMakeGrid)     
        if ((indexCol+1) < len(array2DToMakeGrid[0])-1) and array2DToMakeGrid[indexRow][indexCol+1] != 3 :
            array2DToMakeGrid[indexRow][indexCol]=0
            total=sumscore(allFruitsAndEnimy,indexCol,indexRow)
            if array2DToMakeGrid[indexRow][indexCol+1] == 8:
                lose=True
                endgame()
            if not lose:
                array2DToMakeGrid[indexRow][indexCol+1] = 2  
                # winsound.PlaySound("sounds\\fruit.wav",winsound.SND_FILENAME)
            if total>=5000:
                lose=True
                endgame()
    canvas.delete("all")     
    makeGrid()
    displayresult()
#========================  Move player to left ===========================
def moveLeft(event):
    global Score,lose,won,array2DToMakeGrid
    if not lose:
        indexCol = findCol(array2DToMakeGrid)
        indexRow = findRow(array2DToMakeGrid)
        if indexCol>1 and array2DToMakeGrid[indexRow][indexCol-1] != 3 :
            array2DToMakeGrid[indexRow][indexCol]=0
            total=sumscore(allFruitsAndEnimy,indexCol,indexRow)
            if array2DToMakeGrid[indexRow][indexCol-1] == 8:
                lose=True
                endgame()
            if not lose:
                array2DToMakeGrid[indexRow][indexCol-1] = 2
                # winsound.PlaySound("sounds\\fruit.wav",winsound.SND_FILENAME)
            if total>=5000:
                lose=True
                endgame() 
    canvas.delete("all")
    makeGrid()
    displayresult()
#========================  Move player up ===========================
def moveUp(event):
    global Score,lose,won,array2DToMakeGrid
    if not lose:
        indexCol = findCol(array2DToMakeGrid)
        indexRow = findRow(array2DToMakeGrid)
        if indexRow>1 and array2DToMakeGrid[indexRow-1][indexCol] != 3:
            array2DToMakeGrid[indexRow][indexCol]=0
            total=sumscore(allFruitsAndEnimy,indexCol,indexRow)
            if array2DToMakeGrid[indexRow-1][indexCol] == 8:
                lose=True
                endgame()
            if not lose:
                array2DToMakeGrid[indexRow-1][indexCol] = 2
                # winsound.PlaySound("sounds\\fruit.wav",winsound.SND_FILENAME)
            if total>=5000:
                lose=True
                endgame() 
    canvas.delete("all")
    makeGrid()
    displayresult()

#========================  Move player down ===========================
def moveDown(event):
    global Score,lose,won,array2DToMakeGrid
    if not lose:
        indexCol = findCol(array2DToMakeGrid)
        indexRow = findRow(array2DToMakeGrid)          
        if indexRow+1 < len(array2DToMakeGrid[0])-1 and (array2DToMakeGrid[indexRow+1][indexCol] != 3 and array2DToMakeGrid[indexRow+1][indexCol] != 1) :
            array2DToMakeGrid[indexRow][indexCol]=0
            total=sumscore(allFruitsAndEnimy,indexCol,indexRow)
            if array2DToMakeGrid[indexRow+1][indexCol] == 8:
                lose=True
                endgame()
            if not lose:
                array2DToMakeGrid[indexRow+1][indexCol] = 2
                # winsound.PlaySound("sounds\\fruit.wav",winsound.SND_FILENAME)
            if total>=5000:
                lose=True
                endgame() 
    canvas.delete("all")
    makeGrid()
    displayresult()
makeGrid()   

#============================   Player type on the four arrows such as up, down, right and left  =============
root.bind("<Right>",moveRight)   
root.bind("<Left>",moveLeft)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)

canvas.create_image(490,260,image=firstBackground,anchor="center")
#=======================  The three level  ===========================================
def startlevel(event):
    global background
#=======================  guide player in to easy level  ===================================
    canvas.create_image(0,0,image=firstBackground,anchor="nw")
    canvas.create_text(480,100,text="Welcome To Our Game!",fill="#151B54",font="Time 30 bold")
    canvas.create_rectangle(400, 220, 550, 280, fill="#151B54",outline="white",tags="easy")
    canvas.create_text(480, 250, text = "Easy", fill="#FFFFFF", font="Times 20 bold", tags="easy")

#=======================  guide player in to medium level  =================================
    canvas.create_rectangle(400, 320, 550, 380, fill="#151B54",outline="white",tags="medium")
    canvas.create_text(480,350, text = "Medium", fill="#FFFFFF", font="Times 20 bold", tags="medium")

#=======================  guide player in to difficult level  ===============================
    canvas.create_rectangle(400, 420, 550, 480, fill="#151B54",outline="white",tags="difficult")
    canvas.create_text(480, 450, text = "Difficult", fill="#FFFFFF", font="Times 20 bold", tags="difficult")

#=======================  The first interface to click start  =========================
def startgame():
    canvas.create_image(0,0,image=firstBackground,anchor="nw")
    canvas.create_text(530,100,text="Welcome To Maze Game",font="Time 30 bold",fill="#151B54")
    canvas.create_image(360, 200, image=character,anchor="nw")
    canvas.create_text(500,280,text="Vs",font="Time 30 bold",fill="#151B54")
    canvas.create_image(530, 200, image=cAnemy1,anchor="nw")
    canvas.create_rectangle(420,400,550,460,fill="#151B54",tags="start")
    canvas.create_text(485,430,text="START",fill="#FFFFFF",font="Time 20 bold",tags="start")
startgame()
# ===========================  All button which guide user click on and start game  ====================
canvas.tag_bind("start","<Button-1>",startlevel)
canvas.tag_bind("easy","<Button-1>",easy)
canvas.tag_bind("medium","<Button-1>",medium)
canvas.tag_bind("difficult","<Button-1>",difficult)
canvas.tag_bind("exit","<Button-1>",startlevel)


canvas.pack(expand=True, fill= "both")
surface.pack(expand=True, fill = "both")
surface.mainloop()
