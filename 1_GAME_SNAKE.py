import turtle as T 
import mysql.connector as mc
obj=mc.connect(host='localhost',user='root',password='Prerna@1004',database='game')
obj_1=mc.connect(host='localhost',user='root',password='Prerna@1004',database='quiz')
cursor=obj.cursor()
cursor_1=obj_1.cursor()

import tkinter.messagebox
import FINAL_HOMEPAGE_TOYCATHON
import random
from random import randrange
from random import randint
from freegames import square, vector
import pygame
global F1
global F2
global F3
global F4
global F5
global ans
global prerna
from FINAL_HOMEPAGE_TOYCATHON import username_1
print(username_1)



prerna=0
F1,F2,F3,F4,F5,ans=0,0,0,0,0,0
pen = T.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
##pen.goto(0, 260)
##pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

#print('INSTRUCTIONS:\n\n 1.The snake moves horizontally and vertically \n\n 2.There is a questions displayed on the top left corner and there are various food boxes on which different numbers are printed\n\n 3.The correct answer to the questions is printed on one of those food boxes\n\n 4.The snake is supposed to eat the food in which the correct nawer for the questions is printed \n\n 5.Any consumption of the food containing wrong answer for the questions ends the game \n\n 6.In case of a division question ,the answer contains only the whole number part and not the decimal.make sure you notice this \n\n ALL THE BEST !')
T.bgcolor('#00cc00')
#T.bgpic('grass.jpg')

def add():
    x=randint(-20,20)
    y=randint(-20,20)
   
    global ans
    ans=x+y
    global F1
    F1=randint(-200,200)
    global F2
    F2=randint(-200,200)
    global F3
    F3=randint(-200,200)
    global F4
    F4=randint(-200,200)
    global F5
    F5=randint(-200,200)
    #print("Find",x,"+",y,"=?")
    x1=str(x)
    y1=str(y)
    global prerna
    
    pen.goto(-315,240)
    pen.clear()
    pen.write("Find "+x1+"+"+"("+y1+")"+"=?",font=("Arial", 20, "normal"))
    pen.goto(75,240)
    pen.write("Your Score:",font=("Arial", 20, "normal"))
def sub():
    x=randint(-20,20)
    y=randint(-20,20)
        
    global ans
    ans=x-y
    global F1
    F1=randint(-200,200)
    global F2
    F2=randint(-200,200)
    global F3
    F3=randint(-200,200)
    global F4
    F4=randint(-200,200)
    global F5
    F5=randint(-200,200)
    #print("Find",x,"-",y,"=?")
    x1=str(x)
    y1=str(y)
    global prerna
    
    pen.goto(-315,240)
    pen.clear()
    pen.write("Find "+x1+"-"+"("+y1+")"+"=?",font=("Arial", 20, "normal"))
    pen.goto(75,240)
    pen.write("Your score:"+str(prerna)+"",font=("Arial", 20, "normal"))
def mult():
    x=randint(-20,20)
    y=randint(-20,20)
    
    global F1
    F1=randint(-200,200)
    global F2
    F2=randint(-200,200)
    global F3
    F3=randint(-200,200)
    global F4
    F4=randint(-200,200)
    global F5
    F5=randint(-200,200)
    global ans
    ans=x*y
    #print("Find",x,"x",y,"=?")
    x1=str(x)
    y1=str(y)
    global prerna
    
    pen.goto(-315,240)
    pen.clear()
    pen.write("Find "+x1+"x"+"("+y1+")"+"=?",font=("Arial", 20, "normal"))
    pen.goto(75,240)
    pen.write("Your score:"+str(prerna)+"",font=("Arial", 20, "normal"))
def div():
    x=randint(-20,20)
    y=randint(-20,20)
    
    global ans
    
    if x%y==0:
        ans=(x//y)
    else:
        ans=round((x/y),2)
    global F1
    F1=randint(-200,200)
    global F2
    F2=randint(-200,200)
    global F3
    F3=randint(-200,200)
    global F4
    F4=randint(-200,200)
    global F5
    F5=randint(-200,200)
    #print("Find",x,"/",y,"=?")
    x1=str(x)
    y1=str(y)
    global prerna

    pen.goto(-315,240)
    pen.clear()
    pen.write("Find "+x1+"/"+"("+y1+")"+"=?",font=("Arial", 20, "normal"))
    pen.goto(75,240)
    pen.write("Your score:"+str(prerna)+"",font=("Arial", 20, "normal"))
Ran=randint(1,5)
if Ran==1:
    add()
elif Ran==2:
    sub()
elif Ran==3:
    mult()
elif Ran==4:
    div()

    
count,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12=0,(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10),(randrange(-20,20)*10)

f1,f2,f3,f4,f5,f6 = vector(c1, c2),vector(c3,c4),vector(c5, c6),vector(c7, c8),vector(c9, c10),vector(c11, c12)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -335 < head.x < 320 and -280 < head.y < 280

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    global prerna
    global username
    if not inside(head) or head in snake or head==f1 or head==f2 or head==f3 or head==f4 or head==f5:
        square(head.x, head.y, 15, 'red')
        #exit()
        
        #sunita ma'am
        ##from FINAL_HOMEPAGE_TOYCATHON import username
        #print(username)
        #cursor.execute("insert into snake values("+username+","+str(prerna)+")")
        tkinter.messagebox.showinfo("Game Over","GAME OVER!\nThank you for playing")
        T.update()
        return

    snake.append(head)

    if head == f6:
        #global prerna
        prerna=prerna+10 
        #print('Snake:', len(snake))
        Ran=randint(1,5)
        if Ran==1:
            add()
        elif Ran==2:
            sub()
        elif Ran==3:
            mult()
        elif Ran==4:
            div()
        
        f1.x = randrange(-20, 20) * 10
        f1.y = randrange(-20, 20) * 10
        f2.x = randrange(-20, 20) * 10
        f2.y = randrange(-20, 20) * 10
        f3.x = randrange(-20, 20) * 10
        f3.y = randrange(-20, 20) * 10
        f4.x = randrange(-20, 20) * 10
        f4.y = randrange(-20, 20) * 10
        f5.x = randrange(-20, 20) * 10
        f5.y = randrange(-20, 20) * 10
        f6.x = randrange(-20, 20) * 10
        f6.y = randrange(-20, 20) * 10

    else:
        snake.pop(0)

    T.clear()

    for body in snake:
        square(body.x, body.y, 20, 'yellow')
       


    s=randint(-100,100)
    square(f1.x, f1.y, 20, 'crimson')
    square(f2.x, f2.y, 20, 'crimson')
    square(f3.x, f3.y, 20, 'crimson')
    square(f4.x, f4.y, 20, 'crimson')
    square(f5.x, f5.y, 20, 'crimson')
    square(f6.x, f6.y, 20, 'crimson')
   
    pen.goto(f6.x,f6.y)
    pen.write(ans,font=("Arial", 12, "normal"))
    pen.goto(f5.x,f5.y)
    pen.write(F5,font=("Arial", 12, "normal"))
    pen.goto(f4.x,f4.y)
    pen.write(F4,font=("Arial", 12, "normal"))
    pen.goto(f3.x,f3.y)
    pen.write(F3,font=("Arial", 12, "normal"))
    pen.goto(f2.x,f2.y)
    pen.write(F2,font=("Arial", 12, "normal"))
    pen.goto(f1.x,f1.y)
    pen.write(F1,font=("Arial", 12, "normal"))
    T.update()
    T.ontimer(move, 100)
    
    


T.hideturtle()
T.tracer(False)
T.listen()
T.onkey(lambda: change(10, 0), 'Right')
T.onkey(lambda: change(-10, 0), 'Left')
T.onkey(lambda: change(0, 10), 'Up')
T.onkey(lambda: change(0, -10), 'Down')
move()
T.done()
