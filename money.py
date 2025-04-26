import random
import tkinter.messagebox
from tkinter import *
global z
global x
global y
global a
global b
global c
global A
global B
global C
global f1
global f2
global f3
global f4
global f5
global f6
global f7
global f8
global root1
global root2
global root3
global root4
global root5
global var
global b1
global b2
global b3
global b4
global b5
global b6
global b7
global b8
global b9
global b10
global b11
global c1
global c2
global c3
global c4
global c5
global c6
global c7
global c8
global c9
global c10
global c11
global radio
global radio1
global radio2
global d1
global d2
global d3
global d4
global d5
global d6
global d7
global d8
global d9
global d10
global d11
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
global e9
global e10
global e11
z=0
x=0
y=0
#var=IntVar()

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
f5=random.randrange(1,5,1)
f6=str(random.randrange(0,9,1))
f7=str(random.randrange(0,9,1))
f8=str(random.randrange(0,9,1))
def first():
    global root1
    global var
    global f5
    global f4
    global f3
    global f2
    global f1
    global x
    global y
    #var = IntVar()
    #var.set(None)
    root1=Tk()
    root1.geometry("1000x250")
    root1.configure(bg='Yellow')
    root1.title("money bender")
    var=IntVar()
    Label(root1,text='Q1:Calculate the simple interest if principle amount is '+A+' ,rate of interest on the principal amount is '+B+' ,\nand the duration is '+C+' years?',font="lucida 14 bold",justify=LEFT,padx=20,bg='light coral').pack()
    if f5==1:
        radio=Radiobutton(root1,text='₹'+f1+'.'+f6,padx=14,variable=var,value=1).pack()
        radio=Radiobutton(root1,text='₹'+f2+'.'+f7,padx=14,variable=var,value=2).pack()
        radio=Radiobutton(root1,text='₹'+f3+'.'+f8,padx=14,variable=var,value=3).pack()
        radio=Radiobutton(root1,text='₹'+f4,padx=14,variable=var,value=4).pack()
    elif f5==2:
        radio=Radiobutton(root1,text='₹'+f2+'.'+f7,padx=14,variable=var,value=2).pack()
        radio=Radiobutton(root1,text='₹'+f3+'.'+f8,padx=14,variable=var,value=3).pack()
        radio=Radiobutton(root1,text='₹'+f4,padx=14,variable=var,value=4).pack()
        radio=Radiobutton(root1,text='₹'+f1+'.'+f6,padx=14,variable=var,value=1).pack()
    elif f5==3:
        radio=Radiobutton(root1,text='₹'+f3+'.'+f6,padx=14,variable=var,value=3).pack()
        radio=Radiobutton(root1,text='₹'+f4,padx=14,variable=var,value=4).pack()
        radio=Radiobutton(root1,text='₹'+f1+'.'+f8,padx=14,variable=var,value=1).pack()
        radio=Radiobutton(root1,text='₹'+f2+'.'+f7,padx=14,variable=var,value=2).pack()
    elif f5==4:
        radio=Radiobutton(root1,text='₹'+f4,padx=14,variable=var,value=4).pack()
        radio=Radiobutton(root1,text='₹'+f1+'.'+f8,padx=14,variable=var,value=1).pack()
        radio=Radiobutton(root1,text='₹'+f2+'.'+f7,padx=14,variable=var,value=2).pack()
        radio=Radiobutton(root1,text='₹'+f3+'.'+f6,padx=14,variable=var,value=3).pack()
    Button(root1,text="Next",command=first_redirect,bg='cyan',fg='red',font=("Arial Bold",20)).pack()
    #root1.mainloop()
    mainloop()
########################################################################
def first_redirect():
    global root1
    global var
    global x
    global y
    global z
    if var.get()==4:
        tkinter.messagebox.showinfo("Money Bender","Your answer is correct")
        print("your answer is correct")
        z=z+5
        x=x+1
    else :
        print('your answer is wrong')
        tkinter.messagebox.showinfo("Money Bender","Your answer is wrong\nthe correct answer is "+str(f4))
        y=y+1
    root1.destroy()
    second()
    mainloop()
############################################################################
def second():
    global root2
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global b10
    global b11
    global d1
    global d2
    global d3
    global d4
    global d5
    global d6
    global d7
    global d8
    global d9
    global d10
    global d11
    global radio1
    global radio2
    global var
    global x
    global y
    global z
    global root1
    #var = StringVar()
    #var.set(None)
    #root1.destroy()
    root2=Tk()
    root2.geometry("1000x250")
    root2.configure(bg='Yellow')
    root2.title("money bender")
    var=IntVar()
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
    Label(root2,text='Q2:The percentage profit earned by selling an article for Rs.'+d4+' is equal to the percentage loss incurred by \nselling the same article for Rs.'+d5+'. At what price should the article be sold to make'+d6+'profit?',font="lucida 14 bold",justify=LEFT,padx=14,bg='light coral').pack()
    if d7==1:
        radio=Radiobutton(root2,text='₹'+d8,padx=14,variable=var,value=11).pack()
        radio=Radiobutton(root2,text='₹'+d9,padx=14,variable=var,value=12).pack()
        radio=Radiobutton(root2,text='₹'+d10,padx=14,variable=var,value=13).pack()
        radio=Radiobutton(root2,text='₹'+d11,padx=14,variable=var,value=14).pack()
    if d7==2:
        radio=Radiobutton(root2,text='₹'+d9,padx=14,variable=var,value=12).pack()
        radio=Radiobutton(root2,text='₹'+d10,padx=14,variable=var,value=13).pack()
        radio=Radiobutton(root2,text='₹'+d11,padx=14,variable=var,value=14).pack()
        radio=Radiobutton(root2,text='₹'+d8,padx=14,variable=var,value=11).pack()
    if d7==3:
        radio=Radiobutton(root2,text='₹'+d10,padx=14,variable=var,value=13).pack()
        radio=Radiobutton(root2,text='₹'+d11,padx=14,variable=var,value=14).pack()
        radio=Radiobutton(root2,text='₹'+d8,padx=14,variable=var,value=11).pack()
        radio=Radiobutton(root2,text='₹'+d9,padx=14,variable=var,value=12).pack()
    if d7==4:
        radio=Radiobutton(root2,text='₹'+d11,padx=14,variable=var,value=14).pack()
        radio=Radiobutton(root2,text='₹'+d8,padx=14,variable=var,value=11).pack()
        radio=Radiobutton(root2,text='₹'+d9,padx=14,variable=var,value=12).pack()
        radio=Radiobutton(root2,text='₹'+d10,padx=14,variable=var,value=13).pack()
    Button(root2,text="Next",command=second_redirect,bg='cyan',fg='red',font=("Arial Bold",20)).pack()
    #root2.mainloop()
    mainloop()
##################################################################################
def second_redirect():
    global root2
    global var
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global x
    global y
    global z
    if var.get()==11:
        print('your answer is right')
        tkinter.messagebox.showinfo("Money Bender","Your answer is right")
        z=z+5
        x=x+1
    else:
        print('your answer is wrong')
        tkinter.messagebox.showinfo("Money Bender","Your answer is wrong\nThe correct answer is "+d8)
        y=y+1
    
    root2.destroy()
    third()
    mainloop()
########################################################################################
def third():
    global root3
    global var
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global c11
    global x
    global y
    global z
    global d1
    global d2
    global d3
    global d4
    global d5
    global d6
    global d7
    global d8
    global d9
    global d10
    global d11
    #var = StringVar()
    #var.set(None)
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
    root3=Tk()
    root3.geometry("1000x250")
    root3.configure(bg='Yellow')
    root3.title("money bender")
    var=IntVar()
    Label(root3,text='Q3:When a plot is sold for Rs. '+c5+', the owner loses '+c4+'%. At what price must that plot be sold in \n order to gain '+c4+'%?',font="lucida 14 bold",justify=LEFT,padx=14,bg='light coral').pack()
    if c11==1:
        radio=Radiobutton(root3,text='₹'+c7,padx=14,variable=var,value=7).pack()
        radio=Radiobutton(root3,text='₹'+c8,padx=14,variable=var,value=8).pack()
        radio=Radiobutton(root3,text='₹'+c9,padx=14,variable=var,value=9).pack()
        radio=Radiobutton(root3,text='₹'+c10,padx=14,variable=var,value=10).pack()
    elif c11==2:
        radio=Radiobutton(root3,text='₹'+c8,padx=14,variable=var,value=8).pack()
        radio=Radiobutton(root3,text='₹'+c9,padx=14,variable=var,value=9).pack()
        radio=Radiobutton(root3,text='₹'+c10,padx=14,variable=var,value=10).pack()
        radio=Radiobutton(root3,text='₹'+c7,padx=14,variable=var,value=7).pack()
    elif c11==3:
        radio=Radiobutton(root3,text='₹'+c9,padx=14,variable=var,value=9).pack()
        radio=Radiobutton(root3,text='₹'+c10,padx=14,variable=var,value=10).pack()
        radio=Radiobutton(root3,text='₹'+c7,padx=14,variable=var,value=7).pack()
        radio=Radiobutton(root3,text='₹'+c8,padx=14,variable=var,value=8).pack()
    elif c11==4:
        radio=Radiobutton(root3,text='₹'+c10,padx=14,variable=var,value=10).pack()
        radio=Radiobutton(root3,text='₹'+c7,padx=14,variable=var,value=7).pack()
        radio=Radiobutton(root3,text='₹'+c8,padx=14,variable=var,value=8).pack()
        radio=Radiobutton(root3,text='₹'+c9,padx=14,variable=var,value=9).pack()
    Button(root3,text="Next",command=third_redirect,bg='cyan',fg='red',font=("Arial Bold",20)).pack()
    #root3.mainloop()
    mainloop()
#######################################################################################
def third_redirect():
    global var
    global x
    global y
    global z
    global root3
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    if var.get()==10:
        print('your answer is right')
        tkinter.messagebox.showinfo("Money Bender","Your answer is right")
        z=z+5
        x=x+1
    else:
        print('your answer is wrong')
        tkinter.messagebox.showinfo("Money Bender","Your answer is wrong\nThe correct answer is "+c10)
        y=y+1
    root3.destroy()
    fourth()
    mainloop()

##########################################################################

def fourth():
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global root4
    global var
    #var=None
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
    root4=Tk()
    root4.geometry("1000x250")
    root4.configure(bg='Yellow')
    root4.title("money bender")
    var=IntVar()
    Label(root4,text='Q4:On selling'+e4+'balls at Rs'+e5+' there is a loss equal to the cost price of'+e6+'balls. The cost price of a ball is?',font="lucida 14 bold",justify=LEFT,padx=14,bg='light coral').pack()
    if e7==1:
        radio=Radiobutton(root4,text='₹'+e8,padx=14,variable=var,value=15).pack()
        radio=Radiobutton(root4,text='₹'+e9,padx=14,variable=var,value=16).pack()
        radio=Radiobutton(root4,text='₹'+e10,padx=14,variable=var,value=17).pack()
        radio=Radiobutton(root4,text='₹'+e11,padx=14,variable=var,value=18).pack()
    if e7==2:
        radio=Radiobutton(root4,text='₹'+e9,padx=14,variable=var,value=16).pack()
        radio=Radiobutton(root4,text='₹'+e10,padx=14,variable=var,value=17).pack()
        radio=Radiobutton(root4,text='₹'+e11,padx=14,variable=var,value=18).pack()
        radio=Radiobutton(root4,text='₹'+e8,padx=14,variable=var,value=15).pack()
    if e7==3:
        radio=Radiobutton(root4,text='₹'+e10,padx=14,variable=var,value=17).pack()
        radio=Radiobutton(root4,text='₹'+e11,padx=14,variable=var,value=18).pack()
        radio=Radiobutton(root4,text='₹'+e8,padx=14,variable=var,value=15).pack()
        radio=Radiobutton(root4,text='₹'+e9,padx=14,variable=var,value=16).pack()
    if e7==4:
        radio=Radiobutton(root4,text='₹'+e11,padx=14,variable=var,value=18).pack()
        radio=Radiobutton(root4,text='₹'+e8,padx=14,variable=var,value=15).pack()
        radio=Radiobutton(root4,text='₹'+e9,padx=14,variable=var,value=16).pack()
        radio=Radiobutton(root4,text='₹'+e10,padx=14,variable=var,value=17).pack()
    Button(root4,text="Next",command=fourth_redirect,bg='cyan',fg='red',font=("Arial Bold",20)).pack()
    #root4.mainloop()
    mainloop()
###########################################################################
def fourth_redirect():
    global var
    global x
    global y
    global z
    global root4
    if var.get()==15:
        print('your answer is right')
        tkinter.messagebox.showinfo("Money Bender","Your answer is right")
        z=z+5
        x=x+1
    else:
        print('your answer is wrong')
        tkinter.messagebox.showinfo("Money Bender","Your answer is wrong\nThe correct answer is "+e8)
        y=y+1
    root4.destroy()
    mains()
    mainloop()
################################################################################
def close():
    exit()
#################################################################################
def mains():
    global x
    global y
    global z
    global root5
    root5=Tk()
    root5.geometry("1000x500")
    root5.configure(bg='Cyan')
    root5.title("money bender")
    print('you total score is',z,'correct answers:',x,'wrong answers:',y)
    Label(root5,text='YOUR TOTAL SCORE IS:'+str(z),justify=LEFT,padx=14,font=("Arial Bold",50),bg='red').pack()
    Label(root5,text='Correct answers:'+str(x),justify=LEFT,padx=14,font=("Arial Bold",50)).pack()
    Label(root5,text='Wrong answers:'+str(y),justify=LEFT,padx=14,font=("Arial Bold",50)).pack()
    Button(root5,text="CLOSE",command=close,bg='black',fg='white',font=("Arial Bold",20)).pack()
first()






