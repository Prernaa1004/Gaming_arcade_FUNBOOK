import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
global root_1
global win1
global win2
global win3
global win4
global username
import random
import mysql.connector as mc
import time
username="word"
global username_1
#tkinter: GUI ,pygame : SNAKE,freegames : SNAKE ,vector,mathplotlib : GRAPH ,turtle : GUI ,mysql.connector : HOMEPAGE

        
def mainscreen1():
    win=Tk()
    win.geometry("720x400")
    l=Label(win,text=" welcome to funbook ")
    l.pack()


def first_game():
    #global win1
    #win1=Tk()
    os.system('GAME_5_UPDATED.py')

def second_game():
    #global win2
    #win2=Tk()
    os.system('5_GAME_QUIZ.py')
    
def third_game():
    #global win3
    #win3=Tk()
    #os.system('1_GAME_SNAKE.py')
    import GAME_SNAKE
    obj=mc.connect(host='localhost',user='root',password='Prerna@1004',database='game')
    cursor=obj.cursor()    
    print(username_1,'permanganate')
    cursor.execute('select * from snake')
    r1=cursor.fetchall()
    print(r1)
    b=0
    for i in r1:
        
        if (username_1)==i[0] and i[1]<GAME_SNAKE.prerna:
            b=1
            break
        elif username_1==i[0] and i[1]>GAME_SNAKE.prerna: 
            b=2
            break
    if b==1:
        variable=("update snake set high_score={} where name='{}'")
        cursor.execute(variable.format(GAME_SNAKE.prerna,username_1))
        obj.commit()
        cursor.execute('select * from snake')
        print(cursor.fetchall(),"signal")
    elif b!=2:
        cursor.execute("insert into snake values('{}','{}')".format(username_1,(GAME_SNAKE.prerna)))
        obj.commit()

    
            

def fourth_game():
    #global win4
    #win4=Tk()
    os.system('bar_graph.py')


def fifth_game():
    #global win4
    #win4=Tk()
    os.system('quiz_final.py')
        
def home_page():
    global root_1
    root_1 = tk.Toplevel()
    

    
    global bg_1,icon1,icon2,icon3,icon4,icon5
    bg_1 = PhotoImage(file="background.png")
    icon1=PhotoImage(file="memory.png")
    icon2=PhotoImage(file="chemlogo.png")
    icon3=PhotoImage(file="snake.png")
    icon4=PhotoImage(file="bar.png")
    icon5=PhotoImage(file="money.png")
    
    canvas_1 = Canvas( root_1, width = 720, height = 400) 
    canvas_1.pack(fill = "both", expand = True) 
    canvas_1.create_image( 0, 0, image = bg_1,anchor = NW) 
    button_1 = Button( root_1, width=90,height=100,text = "GAME 1",command=first_game,image=icon1,font=("Arial Bold",15),bg="yellow",fg="red") 
    button_2 = Button( root_1, width=90,height=100,text = "GAME 2",command=second_game,image=icon2,font=("Arial Bold",15),bg="yellow",fg="red") 
    button_3 = Button( root_1, width=90,height=100,text = "GAME 3",command=third_game,image=icon3,font=("Arial Bold",15),bg="yellow",fg="red")
    button_4 = Button( root_1, width=90,height=100,text = "GAME 4",command=fourth_game,image=icon4,font=("Arial Bold",15),bg="yellow",fg="red")
    button_5 = Button( root_1, width=90,height=100,text = "GAME 5",command=fifth_game,image=icon5,font=("Arial Bold",15),bg="yellow",fg="red")
    #button_6 = Button( root_1, width=90,height=100,text = "LEADERBOARD",command=leaderboard,font=("Arial Bold",15),bg="yellow",fg="red")
    button1_canvas = canvas_1.create_window( 100, 250, anchor = "nw", window = button_1) 
    button2_canvas = canvas_1.create_window( 205, 250, anchor = "nw", window = button_2) 
    button3_canvas = canvas_1.create_window( 310, 250, anchor = "nw", window = button_3)
    button4_canvas = canvas_1.create_window( 415, 250, anchor = "nw", window = button_4)
    button5_canvas = canvas_1.create_window( 520, 250, anchor = "nw", window = button_5)
   # button6_canvas = canvas_1.create_window( 100, 400, anchor = "nw", window =button_6) 
    root_1.mainloop()

    
'''def leaderboard():
    root = Tk()
     
    # specify size of window.
    #root.geometry("250x170")
     
    # Create text widget and specify size.
    #T = Text(root, height = 5, width = 52)
     
    # Create label
##    l = Label(root, text = "Fact of the Day")
##    l.config(font =("Courier", 14))
     
    Fact = """A man can be arrested in
    Italy for wearing a skirt in public."""
     
    # Create button for next text.

    
    #T.pack()
     
    # Insert The Fact.
    #T.insert(tk.END, Fact)
     
   
    cursor.execute("select * from snake order by high_score desc;")
    r_4=cursor.fetchall()
    #for i in r_4:
    for i in r_4:
        l = Label(root, text = i)
        l.config(font =("Courier", 14))
        l.pack()
    tk.mainloop()'''
        
        
    




def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="dark blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="light sea green")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Funbook Login",fg="black",bg="light sea green")
    heading.config(font=('garamond 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='black',bg='light sea green')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='black',bg='light sea green')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        global username_1
        
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                username_1=uname.get()
                print(username_1)
                
                #login.destroy()
                home_page()
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='light sea green')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,bg='green',fg='black')
    #sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    #root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="dark blue")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="light sea green")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Funbook SignUp",fg="black",bg="light sea green")
    heading.config(font=('garamond 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='black',bg="light sea green")
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='black',bg="light sea green")
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='black',bg="light sea green")
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='black',bg="light sea green")
    clabel.place(relx=0.215,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    
    def addUserToDataBase():
        a=0
               
        global username
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        conn = mc.connect(host='localhost',user='root',password='Prerna@1004',database='quiz')        
        create = conn.cursor()
        create.execute('select * from usersignup')
        r=create.fetchall()
        
        for i in r:
            
            
            if (username) in i[1]:
                a=1
                break
        if a==1:
            messagebox.showerror("ERROR","Username already exists")
            sup.destroy()
            signUpPage()
        else:
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            mySql_insert_query = """INSERT INTO userSignUp (fullname,username,password,country) VALUES (%s, %s, %s, %s) """
            
            record =(fullname,username,password,country)
            create.execute(mySql_insert_query, record)
            conn.commit()
            
        #create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
        #conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
#        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)
    def gotoLogin():
        conn = mc.connect(host='localhost',user='root',password='Prerna@1004',database='quiz')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have an Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="light sea green",fg='black')
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()
def start():
    signUpPage()
    #mainscreen()
start()
