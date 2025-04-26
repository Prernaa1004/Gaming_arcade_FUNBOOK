import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time

##def loginPage(logdata):
##    sup.destroy()
##    global login
##    login = Tk()
##    
##    user_name = StringVar()
##    password = StringVar()
##    
##    login_canvas = Canvas(login,width=720,height=440,bg="blue")
##    login_canvas.pack()
##
##    login_frame = Frame(login_canvas,bg="white")
##    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
##
##    heading = Label(login_frame,text="Quiz App Login",fg="blue",bg="white")
##    heading.config(font=('calibri 40'))
##    heading.place(relx=0.2,rely=0.1)
##
##    #USER NAME
##    ulabel = Label(login_frame,text="Username",fg='black',bg='white')
##    ulabel.place(relx=0.21,rely=0.4)
##    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
##    uname.config(width=42)
##    uname.place(relx=0.31,rely=0.4)
##
##    #PASSWORD
##    plabel = Label(login_frame,text="Password",fg='black',bg='white')
##    plabel.place(relx=0.215,rely=0.5)
##    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
##    pas.config(width=42)
##    pas.place(relx=0.31,rely=0.5)
##
##    def check():
##        for a,b,c,d in logdata:
##            if b == uname.get() and c == pas.get():
##                menu()
##                break
##        else:
##            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
##            error.place(relx=0.37,rely=0.7)
##    
##    #LOGIN BUTTON
##    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
##    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
##    log.place(relx=0.4,rely=0.6)
##    
##    
##    login.mainloop()
##
##def signUpPage():
##    root.destroy()
##    global sup
##    sup = Tk()
##    
##    fname = StringVar()
##    uname = StringVar()
##    passW = StringVar()
##    country = StringVar()
##    
##    
##    sup_canvas = Canvas(sup,width=720,height=440,bg="blue")
##    sup_canvas.pack()
##
##    sup_frame = Frame(sup_canvas,bg="white")
##    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
##
##    heading = Label(sup_frame,text="Quiz App SignUp",fg="black",bg="white")
##    heading.config(font=('calibri 40'))
##    heading.place(relx=0.2,rely=0.1)
##
##    #full name
##    flabel = Label(sup_frame,text="Full Name",fg='black',bg='white')
##    flabel.place(relx=0.21,rely=0.4)
##    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
##    fname.config(width=42)
##    fname.place(relx=0.31,rely=0.4)
##
##    #username
##    ulabel = Label(sup_frame,text="Username",fg='black',bg='white')
##    ulabel.place(relx=0.21,rely=0.5)
##    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
##    user.config(width=42)
##    user.place(relx=0.31,rely=0.5)
##    
##    
##    #password
##    plabel = Label(sup_frame,text="Password",fg='black',bg='white')
##    plabel.place(relx=0.215,rely=0.6)
##    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
##    pas.config(width=42)
##    pas.place(relx=0.31,rely=0.6)
##    
##    
##    
##    #country
##    clabel = Label(sup_frame,text="Country",fg='black',bg='white')
##    clabel.place(relx=0.215,rely=0.7)
##    c = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = country)
##    c.config(width=42)
##    c.place(relx=0.31,rely=0.7)
##    def addUserToDataBase():
##        
##        fullname = fname.get()
##        username = user.get()
##        password = pas.get()
##        country = c.get()
##        
##        conn = sqlite3.connect('quiz.db')
##        create = conn.cursor()
##        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
##        create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
##        conn.commit()
##        create.execute('SELECT * FROM userSignUp')
##        z=create.fetchall()
##        print(z)
###        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
##        conn.close()
##        loginPage(z)
##    def gotoLogin():
##        conn = sqlite3.connect('quiz.db')
##        create = conn.cursor()
##        conn.commit()
##        create.execute('SELECT * FROM userSignUp')
##        z=create.fetchall()
##        loginPage(z)
##    #signup BUTTON
##    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
##    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
##    sp.place(relx=0.4,rely=0.8)
##
##    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='blue')
##    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
##    log.place(relx=0.4,rely=0.9)
##
##    sup.mainloop()

##def menu():
##    #login.destroy()
##    global menu 
##    menu = Tk()
##    
##    
##    menu_canvas = Canvas(menu,width=720,height=440,bg="blue")
##    menu_canvas.pack()
##
##    menu_frame = Frame(menu_canvas,bg="white")
##    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
##
##    
##    
##    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="#101357") 
##    wel.config(font=('Broadway 22'))
##    wel.place(relx=0.1,rely=0.02)
##    
##    
##    level = Label(menu_frame,text='Select your Difficulty Level !!',bg="white",font="calibri 18")
##    level.place(relx=0.25,rely=0.3)
##    
##    
##    var = IntVar()
##    easyR = Radiobutton(menu_frame,text='Easy',bg="white",font="calibri 16",value=1,variable = var)
##    easyR.place(relx=0.25,rely=0.4)
##    
##    mediumR = Radiobutton(menu_frame,text='Medium',bg="white",font="calibri 16",value=2,variable = var)
##    mediumR.place(relx=0.25,rely=0.5)
##    
##    hardR = Radiobutton(menu_frame,text='Hard',bg="white",font="calibri 16",value=3,variable = var)
##    hardR.place(relx=0.25,rely=0.6)
##    
##    
##    def navigate():
##        
##        x = var.get()
##        print(x)
##        if x == 1:
##            menu.destroy()
##            easy()
##        elif x == 2:
##            menu.destroy()
##            medium()
##        
##        elif x == 3:
##            menu.destroy()
##            difficult()
##        else:
##            pass
##    letsgo = Button(menu_frame,text="Let's Go",bg="white",font="calibri 12",command=navigate)
##    letsgo.place(relx=0.25,rely=0.8)
##    menu.mainloop()
global score
global li

score = 0

global e
#e = Tk()

def easy():
    global e
    
    e = Tk()
    
    
    easy_canvas = Canvas(e,width=800,height=500,bg="crimson")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="yellow")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
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
                    'Q:Calculate the simple interest if principle amount is '+A+' ,\nrate of interest on the principal amount is '+B+' ,and the duration \n is '+C+' years?',
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
        X4,
        d8,
        c10,
        e8
        
     ]
    global li

    li = ['',0,1,2,3]
    x = random.choice(li[1:])
    print(x)
    
    ques = Label(easy_frame,text =easyQ[x][0],font="verdana 14",bg="yellow",fg="dark blue")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    a = Radiobutton(easy_frame,text=easyQ[x][1],fg="dark blue",font="verdana 12",value=easyQ[x][1],variable=var,bg="yellow")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],fg="dark blue",font="verdana 12",value=easyQ[x][2],variable=var,bg="yellow")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQ[x][3],fg="dark blue",font="verdana 12",value=easyQ[x][3],variable=var,bg="yellow")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQ[x][4],fg="dark blue",font="verdana 12",value=easyQ[x][4],variable=var,bg="yellow")
    d.place(relx=0.5,rely=0.72,anchor=CENTER)
    



   
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        global score
        global li
        
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        #if len(li) == 2:
        #    nextQuestion.configure(text='End',command=calc)
                
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
        if (var.get() == X4 or var.get()==d8 or var.get()==c10 or var.get()==e8):
            score=score+1
        display()
    
    submit = Button(easy_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    #nextQuestion = Button(easy_frame,command=display,text="Next")
    #nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
##def medium():
##    
##    global m
##    m = Tk()
##    
##    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
##    med_canvas.pack()
##
##    med_frame = Frame(med_canvas,bg="white")
##    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
##
##    
##    def countDown():
##        check = 0
##        for k in range(10, 0, -1):
##            
##            if k == 1:
##                check=-1
##            timer.configure(text=k)
##            med_frame.update()
##            time.sleep(1)
##            
##        timer.configure(text="Times up!")
##        if check==-1:
##            return (-1)
##        else:
##            return 0
##        
##    global score
##    score = 0
##    
##    mediumQ = [
##                [
##                    "Which of the following is not an exception handling keyword in Python?",
##                     "accept",
##                     "finally",
##                     "except",
##                     "try"
##                ],
##                [
##                    "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
##                    "3",
##                    "5",
##                    "25",
##                    "1"
##                ],
##                [
##                    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
##                    "Error",
##                    "None",
##                    "25",
##                    "2"
##                ],
##                [
##                    "print(0xA + 0xB + 0xC):",
##                    "0xA0xB0xC",
##                    "Error",
##                    "0x22",
##                    "33"
##                ],
##                [
##                    "Which of the following is invalid?",
##                    "_a = 1",
##                    "__a = 1",
##                    "__str__ = 1",
##                    "none of the mentioned"
##                ], 
##            ]
##    answer = [
##            "accept",
##            "1",
##            "25",
##            "33",
##            "none of the mentioned"
##            ]
##    
##    li = ['',0,1,2,3,4]
##    x = random.choice(li[1:])
##    
##    ques = Label(med_frame,text =mediumQ[x][0],font="calibri 12",bg="white")
##    ques.place(relx=0.5,rely=0.2,anchor=CENTER)
##
##    var = StringVar()
##    
##    a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="white")
##    a.place(relx=0.5,rely=0.42,anchor=CENTER)
##
##    b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="white")
##    b.place(relx=0.5,rely=0.52,anchor=CENTER)
##
##    c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="white")
##    c.place(relx=0.5,rely=0.62,anchor=CENTER) 
##
##    d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="white")
##    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
##    
##    li.remove(x)
##    
##    timer = Label(m)
##    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
##    
##    
##    
##    def display():
##        
##        if len(li) == 1:
##                m.destroy()
##                showMark(score)
##        if len(li) == 2:
##            nextQuestion.configure(text='End',command=calc)
##                
##        if li:
##            x = random.choice(li[1:])
##            ques.configure(text =mediumQ[x][0])
##            
##            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
##      
##            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
##      
##            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
##      
##            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
##            
##            li.remove(x)
##            print(li)
##            y = countDown()
##            if y == -1:
##                display()
##
##            
##    def calc():
##        global score
##        if (var.get() in answer):
##            score+=1
##        display()
##    
##    submit = Button(med_frame,command=calc,text="Submit",font="calibri 10")
##    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
##    
##    nextQuestion = Button(med_frame,command=display,text="Next")
##    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
##    
##    y = countDown()
##    if y == -1:
##        display()
##    m.mainloop()
##def difficult():
##    
##       
##    global h
##    h = Tk()
##    
##    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
##    hard_canvas.pack()
##
##    hard_frame = Frame(hard_canvas,bg="white")
##    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
##
##    
##    def countDown():
##        check = 0
##        for k in range(10, 0, -1):
##            
##            if k == 1:
##                check=-1
##            timer.configure(text=k)
##            hard_frame.update()
##            time.sleep(1)
##            
##        timer.configure(text="Times up!")
##        if check==-1:
##            return (-1)
##        else:
##            return 0
##        
##    global score
##    score = 0
##    
##    hardQ = [
##                [
##       "All keywords in Python are in _________",
##        "lower case",
##        "UPPER CASE",
##        "Capitalized",
##        "None of the mentioned"
##    ],
##    [
##        "Which of the following cannot be a variable?",
##        "__init__",
##        "in",
##        "it",
##        "on"
##    ],
##    [
##     "Which of the following is a Python tuple?",
##        "[1, 2, 3]",
##        "(1, 2, 3)",
##        "{1, 2, 3}",
##        "{}"   
##    ],
##    [
##        "What is returned by math.ceil(3.4)?",
##        "3",
##        "4",
##        "4.0",
##        "3.0"
##    ],
##    [
##        "What will be the output of print(math.factorial(4.5))?",
##        "24",
##        "120",
##        "error",
##        "24.0"
##    ] 
##            
##]
##    answer = [
##            "None of the mentioned",
##            "in",
##            "(1,2,3)",
##            "4",
##            "error"
##            ]
##    
##    li = ['',0,1,2,3,4]
##    x = random.choice(li[1:])
##    
##    ques = Label(hard_frame,text =hardQ[x][0],font="calibri 12",bg="white")
##    ques.place(relx=0.5,rely=0.2,anchor=CENTER)
##
##    var = StringVar()
##    
##    a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="white")
##    a.place(relx=0.5,rely=0.42,anchor=CENTER)
##
##    b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="white")
##    b.place(relx=0.5,rely=0.52,anchor=CENTER)
##
##    c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="white")
##    c.place(relx=0.5,rely=0.62,anchor=CENTER) 
##
##    d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="white")
##    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
##    
##    li.remove(x)
##    
##    timer = Label(h)
##    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
##    
##    
##    
##    def display():
##        
##        if len(li) == 1:
##                h.destroy()
##                showMark(score)
##        if len(li) == 2:
##            nextQuestion.configure(text='End',command=calc)
##                
##        if li:
##            x = random.choice(li[1:])
##            ques.configure(text =hardQ[x][0])
##            
##            a.configure(text=hardQ[x][1],value=hardQ[x][1])
##      
##            b.configure(text=hardQ[x][2],value=hardQ[x][2])
##      
##            c.configure(text=hardQ[x][3],value=hardQ[x][3])
##      
##            d.configure(text=hardQ[x][4],value=hardQ[x][4])
##            
##            li.remove(x)
##            print(li)
##            y = countDown()
##            if y == -1:
##                display()
##
##            
##    def calc():
##        global score
##        if (var.get() in answer):
##            score+=1
##        display()
##    
##    submit = Button(hard_frame,command=calc,text="Submit",font="verdana",)
##    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
##    
##    nextQuestion = Button(hard_frame,command=display,text="Next")
##    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
##    
##    y = countDown()
##    if y == -1:
##        display()
##    h.mainloop()


global sh
#sh = Tk()
    
def showMark(mark):
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=700,height=500,bg="crimson")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="yellow")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Your score is 5"#+str(mark)
    mlabel = Label(show_canvas,text=st,fg="dark blue",font="verdana 20")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    sh.mainloop()

global root 
#root = Tk()
def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 350,height =350)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="moneypic.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = easy) 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
start()
