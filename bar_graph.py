from matplotlib import pyplot as plt
import random
import statistics
import numpy as np
from tkinter import *
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 

global canvas
global toolbar
global root
global p1
global p2
global p3
global y1
y1=random.randrange(1,20)
global y2
y2=random.randrange(1,20)
global y3
y3=random.randrange(1,20)
global y4
y4=random.randrange(1,20)
global y5
y5=random.randrange(1,20)
global y7
global Y1
global Y
global left
global height
global tick_label
global a1
global a2
global a3
global a4
global a5
global a6
def cm_to_inch(value):
    return value/2.54

def graph():
    global p1
    global p2
    global p3
    p1=0
    p2=0
    p3=0
    global y1
    global y2
    global y3
    global y4
    global y5
    global y7
    global Y1
    global Y
    global left
    global height
    global tick_label
    global canvas
    global toolbar

    fig=plt.figure(figsize=(5,4))
    left = [1,2,3,4,5] 
    height = [y1,y2,y3,y4,y5] 
    tick_label = ['pista', 'butterscotch', 'mango', 'vanilla','chocolate' ]
    plt.yticks(np.arange(0,21,1))
    plt.bar(left, height, tick_label = tick_label,width = 0.6, color = ['green','yellow', 'red','blue','brown']) 
    plt.xlabel('flavours of ice-cream') 
    plt.ylabel('no. of students') 
    plt.title('bar chart for students choosing different ice-creams')
    canvas = FigureCanvasTkAgg(fig,master = root)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().grid(row=8,column=1) 
  
    # creating the Matplotlib toolbar 
    #toolbar = NavigationToolbar2Tk(canvas, root) 
    #toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().grid(row=8,column=2)
    
# the main Tkinter window 
    #plt.show()

########################################################################################

def result():
    global p1
    global p2
    global p3
    global y1
    global y2
    global y3
    global y4
    global y5
    global y7
    global Y1
    global Y
    global left
    global height
    global tick_label
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global height
    #a1=int(input('How many birch trees did arthur see:'))
##    print(a1.get())
##    print(type(a1))
##    print(y2)
##    print(type(y2))
    
    if int(a1.get())==(y2):
        print('correct!')
        p1=p1+5
        p2=p2+1
    else:
        print('wrong!')
        p3=p3+1
    #a2=(input('Which tree did he see least:'))
    
    A=min(height)
    print(A)
    print(type(A))
    print(y1)
    print(type(y1))
    print(y2)
    print(type(y2))

    print(y3)
    print(type(y3))

    print(y4)
    print(type(y4))

    print(y5)
    print(type(y5))
    
    
    
    
    if A==y1:
        if (a2.get()).upper()==('chocolate').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    elif A==y2:
        if (a2.get()).upper()==('butterscotch').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    elif A==y3:
        if (a2.get()).upper()==('mango').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    elif A==y4:
        if (a2.get()).upper()==('vanilla').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    elif A==y5:
        if (a2.get()).upper()==('pista').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    else:
        print('invalid input')

        

    #a4=int(input('how many cedar and pine trees together'))
    if int(a4.get())==(y4+y5):
        print('correct!')
        p1=p1+5
        p2=p2+1
    else:
        print('wrong!')
        p3=p3+1

    #a5=int(input('If arthur counted 7 more pine treee how many did he total count:'))
        
    if int(a5.get())==(y4+7): 
        print('correct!')
        p1=p1+5
        p2=p2+1
    else:
        print('wrong!')
        p3=p3+1


    #a6=(input('Which tree did he see most:'))
    B=max(height)
    if B==y1:
        if (a6.get()).upper()==('chocolate').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    elif B==y2:
        if (a6.get()).upper()==('butterscotch').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    elif B==y3:
        if (a6.get()).upper()==('mango').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    elif B==y4:
        if (a6.get()).upper()==('vanilla').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else: 
            print('wrong!')
            p3=p3+1
    elif B==y5:
        if (a6.get()).upper()==('pista').upper():
            print('correct!')
            p1=p1+5
            p2=p2+1
        else:
            print('wrong!')
            p3=p3+1
    else:
        print('invalid input')
    print('Your total score is ',p1,' ,correct answers:',p2,' ,wrong answers:',p3)
    p1=str(p1)
    tkinter.messagebox.showinfo("Score Card","Your total score is:"+p1)

#################################################################################
p1=0
p2=0
p3=0
y1=random.randrange(3,21,1)
y2=random.randrange(4,21,1)
y3=random.randrange(5,21,1)
y4=random.randrange(4,21,1)
y5=random.randrange(3,21,1)
y7=random.randint(3,20)
Y1=random.choice([y1,y2,y3,y4,y5])
Y=str(Y1)

root=Tk()
#root.attributes('-fullscreen', True) 
root.configure(bg='orange')
root.title("Graphical genius")
root.geometry("1350x800")

a1=IntVar()
a2=StringVar()
a3=StringVar()
a4=IntVar()
a5=IntVar()
a6=StringVar()

#L1=Label(root,text="GRAPH GAME",bg='yellow',fg='red',font="lucida 15 bold").grid(columnspan=2)
b1=Button(root,text="SHOW GRAPH",command=graph,bg='crimson',fg='white',font="verdana 20 bold").grid(columnspan=1)

L2=Label(root,text='How many students liked butterscotch:',fg='dark blue',font='verdana 12 bold').grid(row=2,column=0)
T1=Entry(root,textvariable=a1).grid(row=2,column=1,padx=20,pady=10,ipadx=15,ipady=2)

L3=Label(root,text='Which flavour was least liked:',fg='dark blue',font='verdana 12 bold').grid(row=3,column=0)
T2=Entry(root,textvariable=a2).grid(row=3,column=1,padx=20,pady=10,ipadx=15,ipady=2)

##L4=Label(root,text="Which tree did they count "+Y+" of:",fg='green',font='lucida 15 bold').grid(row=4,column=0)
##T3=Entry(root,textvariable=a3).grid(row=4,column=1,padx=20,pady=10,ipadx=15,ipady=5)
##
L5=Label(root,text='how many students liked pista and vanilla together:',fg='dark blue',font='verdana 12 bold').grid(row=5,column=0)
T4=Entry(root,textvariable=a4).grid(row=5,column=1,padx=20,pady=10,ipadx=15,ipady=2)

L6=Label(root,text='If 7 more vanilla choosers were counted,what is the total:',fg='dark blue',font='verdana 12 bold').grid(row=6,column=0)
T5=Entry(root,textvariable=a5).grid(row=6,column=1,padx=20,pady=10,ipadx=15,ipady=2)

L7=Label(root,text='Which flavour was liked the most:',fg='dark blue',font='verdana 12 bold').grid(row=7,column=0)
T6=Entry(root,textvariable=a6).grid(row=7,column=1,padx=20,pady=10,ipadx=15,ipady=2)

b2=Button(root,text="Submit",command=result,bg='green',fg='white',font="verdana 12 bold").grid(columnspan=1)

root.mainloop()




















































import tkinter
import mysql.connector
window=tkinter.Tk()
window.title("CUSTOMER DETAILS")
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Prerna@1004", database = "journal")
mycursor=mydb.cursor()

def insert():
    global l5
    cid=t1.get()
    cname=t2.get()
    gender=t3.get()
    country=t4.get()
    print(cid,cname,gender,country)
    sql="insert into customer values('{}','{}','{}','{}')".format(cid,cname,gender,country)
    mycursor.execute(sql)
    mydb.commit()
    l5=tkinter.Label(text="RECORD ADDED SUCCESSFULLY",font=("Arial Bold",10))
    l5.grid(column=0,row=8)
def clear():
    global l5
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')
    t4.delete(0,'end')
    l5.destroy()
l1=tkinter.Label(text="ENTER CUSTOMER ID",font=("Arial Bold",10))
l1.grid(column=0,row=0)
l2=tkinter.Label(text="ENTER CUSTOMER NAME",font=("Arial Bold",10))
l2.grid(column=0,row=1)
l3=tkinter.Label(text="ENTER GENDER",font=("Arial Bold",10))
l3.grid(column=0,row=2)
l4=tkinter.Label(text="ENTER COUNTRY",font=("Arial Bold",10))
l4.grid(column=0,row=3)

t1=tkinter.Entry(window,width=20)
t1.grid(column=1,row=0)
t2=tkinter.Entry(window,width=20)
t2.grid(column=1,row=1)
t3=tkinter.Entry(window,width=20)
t3.grid(column=1,row=2)
t4=tkinter.Entry(window,width=20)
t4.grid(column=1,row=3)

b1=tkinter.Button(window,text="ADD RECORD",bg="orange",fg="red",command=insert)
b1.grid(column=0,row=6)
b2=tkinter.Button(window,text="CLEAR",bg="orange",fg="red",command=clear)
b2.grid(column=0,row=7)

window.mainloop()
