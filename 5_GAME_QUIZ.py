from tkinter import *


def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()

    def option():

        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#e6fff5',
            border=0,
            justify='center',

        )
        sel_btn1 = Button(
            text="Element symbols",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Atomic mass",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Non-metals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Metals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Compounds",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Acids,bases and salts",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(6),
        )

##        sel_btn7 = Button(
##            text="Vehicles",
##            width=18,
##            borderwidth=8,
##            font=("", 18),
##            fg="#000000",
##            bg="#99ffd6",
##            cursor="hand2",
##            command=lambda: start_game(7),
##        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=6, column=4, pady=(10, 0), padx=50, )
        #sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+400+100")
    main_window.resizable(0, 0)
    main_window.title("chemistry wizard")
    main_window.configure(background="#e6fff5")
    #main_window.iconbitmap(r'quizee_logo_.ico')

    img0 = PhotoImage(file="chemwizard1.png")
    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        image=img0,
        bg='#e6fff5',
    )
    lab_img.pack(pady=(70, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(40, 20))

    main_window.mainloop()


start_main_page()
