from tkinter import *
from random import *
from tkinter import messagebox
import time

SHAPES_WORD =['H2O', 'NaCl', 'C6H12O6', 'CH3COOH', 'Fe2O3', 'NaHCO3','CaCO3','Na2CO3','CH4','Ca(OH)2','H2SO4']

SHAPES_ANSWER = ['water','sodium chloride','glucose','acetic acid','iron oxide','sodium bicarbonate',
                 'calcium carbonate','sodium carbonate','methane','calcium hydroxide','sulphuric acid']







ran_num = randrange(0, (len(SHAPES_WORD)))
jumbled_rand_word = SHAPES_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        import main_start
        main_start.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(SHAPES_WORD)))
        word.configure(text=SHAPES_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().lower()
        if user_word == SHAPES_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(SHAPES_WORD)))
            word.configure(text=SHAPES_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=SHAPES_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Quizee-Shapes_jumbled_words")
    my_window.configure(background="#e6fff5")
    my_window.iconbitmap(r'quizee_logo_.ico')
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
