from tkinter import *
import os
global root_1
global win1
global win2
global win3
global win4

def first_game():
    #global win1
    #win1=Tk()
    os.system('snake.py')

def second_game():
    #global win2
    #win2=Tk()
    os.system('money.py')
    
def third_game():
    #global win3
    #win3=Tk()
    os.system('bar.py')

def fourth_game():
    #global win4
    #win4=Tk()
    os.system('puzzle.py')


def fifth_game():
    #global win4
    #win4=Tk()
    os.system('main_start.py')
    
def home_page():
    global root_1
    root_1 = Tk() 
    root_1.geometry("720x400") 
    bg_1 = PhotoImage(file = "background.png")
    icon1=PhotoImage(file="snake.png")
    icon2=PhotoImage(file="money.png")
    icon3=PhotoImage(file="bar.png")
    icon4=PhotoImage(file="memory.png")
    icon5=PhotoImage(file="chemlogo.png")
    
    canvas_1 = Canvas( root_1, width = 720, height = 400) 
    canvas_1.pack(fill = "both", expand = True) 
    canvas_1.create_image( 0, 0, image = bg_1,anchor = "nw") 
    button_1 = Button( root_1, width=90,height=100,text = "GAME 1",command=first_game,image=icon1,font=("Arial Bold",15),bg="yellow",fg="red") 
    button_2 = Button( root_1, width=90,height=100,text = "GAME 2",command=second_game,image=icon2,font=("Arial Bold",15),bg="yellow",fg="red") 
    button_3 = Button( root_1, width=90,height=100,text = "GAME 3",command=third_game,image=icon3,font=("Arial Bold",15),bg="yellow",fg="red")
    button_4 = Button( root_1, width=90,height=100,text = "GAME 4",command=fourth_game,image=icon4,font=("Arial Bold",15),bg="yellow",fg="red")
    button_5 = Button( root_1, width=90,height=100,text = "GAME 5",command=fifth_game,image=icon5,font=("Arial Bold",15),bg="yellow",fg="red")
    button1_canvas = canvas_1.create_window( 100, 250, anchor = "nw", window = button_1) 
    button2_canvas = canvas_1.create_window( 205, 250, anchor = "nw", window = button_2) 
    button3_canvas = canvas_1.create_window( 310, 250, anchor = "nw", window = button_3)
    button4_canvas = canvas_1.create_window( 415, 250, anchor = "nw", window = button_4)
    button5_canvas = canvas_1.create_window( 520, 250, anchor = "nw", window = button_5)
    root_1.mainloop()

home_page()
#https://icons8.com/icons/set/number-puzzle
