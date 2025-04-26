import tkinter as tk
from tkinter import *
import random
import time

def easy():
    global e
    e = Tk()
    easy_canvas = Canvas(e,width=800,height=500,bg="crimson")
    easy_canvas.pack()
    easy_frame = Frame(easy_canvas,bg="yellow")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)  
    def countDown():
        check = 0
        for k in range(120, 0, -1):   
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
# first question
    a=random.randrange(100,1000,10)
    b=random.randint(1,50)
    c=random.randint(1,10)

    A=str(a)
    B=str(b)
    C=str(c)

    f1=str(random.randrange(100,1000,1))
    f2=str(random.randrange(100,1000,1))
    f3=str(random.randrange(100,1000,1))
    f4=str((a*b*c)/100)
    f6=str(random.randrange(0,9,1))
    f7=str(random.randrange(0,9,1))
    f8=str(random.randrange(0,9,1))


#2nd question
    d1=random.randrange(6000,10000,100)
    d2=random.randrange(1000,5000,100)
    d3=random.randint(10,90)
    d4=str(d1)
    d5=str(d2)
    d6=str(d3)
    d7=random.randrange(1,5,1)
    d8=str(((d1+d2)//2)*((100+d3)//100))
    d9=str(random.randrange(1000,10000,10))
    d10=str(random.randrange(1000,10000,10))
    d11=str(random.randrange(1000,10000,10))

#3rd question
    c1=random.randint(10,50)
    c2=random.randrange(5000,50000,100)
    c3=random.randint(1,13)
    c4=str(c1)
    c5=str(c2)
    c6=str(c3)
    c7=str(random.randrange(5000,50000,100))
    c8=str(random.randrange(5000,50000,100))
    c9=str(random.randrange(5000,50000,100))
    c10=str(((100+c1)*c2)//(100-c1))
    c11=random.randrange(1,5,1)

#4th question
    e1=random.randint(20,50)
    e2=random.randrange(100,1000,10)
    e3=random.randint(1,13)
    e4=str(e1)
    e5=str(e2)
    e6=str(e3)
    e7=random.randrange(1,5,1)
    e8=str((e2//(e1-e3)))
    e9=str(random.randrange(10,51,1))
    e10=str(random.randrange(10,51,1))
    e11=str(random.randrange(10,51,1))

    X1=f1+'.'+f6
    X2=f2+'.'+f7,
    X3=f3+'.'+f8,
    X4=f4
    X5=[X1,X2,X3,X4]
    
    X6=random.choice(X5)
    X5.remove(X6)
    X7=random.choice(X5)
    X5.remove(X7)
    X8=random.choice(X5)
    X5.remove(X8)
    X9=random.choice(X5)
    X5.remove(X9)

    Y5=[d8,d9,d10,d11]
    
    Y6=random.choice(Y5)
    Y5.remove(Y6)
    Y7=random.choice(Y5)
    Y5.remove(Y7)
    Y8=random.choice(Y5)
    Y5.remove(Y8)
    Y9=random.choice(Y5)
    Y5.remove(Y9)

    Z5=[c7,c8,c9,c10]
    Z6=random.choice(Z5)
    Z5.remove(Z6)
    Z7=random.choice(Z5)
    Z5.remove(Z7)
    Z8=random.choice(Z5)
    Z5.remove(Z8)
    Z9=random.choice(Z5)
    Z5.remove(Z9)
    
    W5=[e8,e9,e10,e11]
    W6=random.choice(W5)
    W5.remove(W6)
    W7=random.choice(W5)
    W5.remove(W7)
    W8=random.choice(W5)
    W5.remove(W8)
    W9=random.choice(W5)
    W5.remove(W9)
    
    easyQ = [
                 [
                    'Q:Calculate the simple interest if principle amount is '+A+' ,\nrate ofinterest on the principal amount is '+B+' ,and the duration \n is '+C+' years?',
                     X6,
                     X7,
                     X8,
                     X9
        
                 ] ,
                 [
                    'Q:The percentage profit earned by selling an article for Rs. '+d4+' \n is equal to the  percentage loss incurred by selling the same\n  article for Rs. '+d5+' . At what price should the article be sold \n to make '+d6+' profit?' ,
                    Y6,
                    Y7,
                    Y8,
                    Y9
                     
                 ],
                [
                    'Q:When a plot is sold for Rs. '+c5+', the owner loses '+c4+'%. \nAt what price must that plot be sold in order to gain '+c4+'%?',
                    Z6,
                    Z7,
                    Z8,
                    Z9
                ],
                [
                    'Q:On selling '+e4+' balls at Rs '+e5+' there is a loss equal to the \n cost price of '+e6+' balls. The cost price of a ball is?' ,
                    W6,
                    W7,
                    W8,
                    W9
                ]
            ]

    answer = [
        f4,
        d8,
        c10,
        e8
        ]
    li = ['',0,1,2,3]
    x = random.choice(li[1:])
    ques = Label(easy_frame,text =easyQ[x][0],font="verdana 14",bg="yellow")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)
    var = StringVar()
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="verdana 12",value=easyQ[x][1],variable = var,bg="yellow")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)
    b = Radiobutton(easy_frame,text=easyQ[x][2],font="verdana 12",value=easyQ[x][2],variable = var,bg="yellow")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)
    c = Radiobutton(easy_frame,text=easyQ[x][3],font="verdana 12",value=easyQ[x][3],variable = var,bg="yellow")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 
    d = Radiobutton(easy_frame,text=easyQ[x][4],font="verdana 12",value=easyQ[x][4],variable = var,bg="yellow")
    d.place(relx=0.5,rely=0.72,anchor=CENTER)
    li.remove(x)
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    def display():
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()
    def calc():
        global score
        if (var.get() in answer):
            score=score+5
        display() 
    submit = Button(easy_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)  
    nextQuestion = Button(easy_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()

def showMark(mark):
    global sh
    sh = Tk()
    show_canvas = Canvas(sh,width=720,height=440,bg="#101357")
    show_canvas.pack()
    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    st = "Your score is "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    sh.mainloop()
    
def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 350,height =350)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="money.png")
    canvas.create_image(50,10,image=img,anchor=NW)
    button = Button(root, text='Start',command = easy) 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)
    root.mainloop()
start()
