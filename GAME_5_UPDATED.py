from tkinter import *


def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            import random
            import tkinter as tk
            import tkinter.messagebox
            from PIL import Image, ImageTk
            import random
            #tk.geometry(1000x1000)
            MAX_BOARD_SIZE = 600
            files=['elephant.jpeg','mango.jpeg','tiger.jpeg','lion.jpeg','peacock.jpeg']
            a=random.choice(files)
            class Application(tk.Frame):

                def __init__(self, image, board_grid=4):
                    tk.Frame.__init__(self)
                    self.grid()
                    self.board_grid = board_grid if board_grid > 2 else 3
                    self.load_image(image)
                    self.steps = 0
                    self.create_widgets()
                    self.create_events()
                    self.create_board()
                    self.show()

                def load_image(self, image):
                    image = Image.open(image)
                    board_size = min(image.size)
                    if image.size[0] != image.size[1]:
                        image = image.crop((0, 0, board_size, board_size))
                    if board_size > MAX_BOARD_SIZE:
                        board_size = MAX_BOARD_SIZE
                        image = image.resize((board_size, board_size), Image.ANTIALIAS)
                    self.image = image
                    self.board_size = board_size
                    self.piece_size = self.board_size / self.board_grid

                def create_widgets(self):
                    args = dict(width=self.board_size, height=self.board_size)
                    self.canvas = tk.Canvas(self, **args)
                    self.canvas.grid(row=0,column=0)
                    
                    #self.canvas = tk.Canvas(width=300, height=300, bg='white')
                    #self.canvas.grid()

                    load = Image.open(a)
                    render = ImageTk.PhotoImage(load)
                    
                    widget = tk.Label(self, image=render, fg='white', bg='black')
                    widget.image = render
                    widget.place(x=0,y=0)
                    widget.grid(row=0,column=1)
                    #self.canvas.create_window(100, 100, window=widget)

                def create_events(self):
                    self.canvas.bind_all('<KeyPress-Up>', self.slide)
                    self.canvas.bind_all('<KeyPress-Down>', self.slide)
                    self.canvas.bind_all('<KeyPress-Left>', self.slide)
                    self.canvas.bind_all('<KeyPress-Right>', self.slide)
                    self.canvas.bind_all('<KeyPress-h>', self.slide)
                    self.canvas.bind_all('<KeyPress-j>', self.slide)
                    self.canvas.bind_all('<KeyPress-k>', self.slide)
                    self.canvas.bind_all('<KeyPress-l>', self.slide)
                    self.canvas.bind_all('<KeyPress-H>', self.help)

                def help(self, event):
                    if getattr(self, '_img_help_id', None) is None:
                        self._img_help = ImageTk.PhotoImage(self.image)
                        self._img_help_id = self.canvas.create_image(0, 0,
                                image=self._img_help, anchor=tk.NW)
                    else:
                        state = self.canvas.itemcget(self._img_help_id, 'state')
                        state = 'hidden' if state == '' else ''
                        self.canvas.itemconfigure(self._img_help_id, state=state)

                def slide(self, event):
                    pieces = self.get_pieces_around()
                    if event.keysym in ('Up', 'k') and pieces['bottom']:
                        self._slide(pieces['bottom'], pieces['center'], 
                                    (0, -self.piece_size))
                    if event.keysym in ('Down', 'j') and pieces['top']:
                        self._slide(pieces['top'], pieces['center'],
                                    (0, self.piece_size))
                    if event.keysym in ('Left', 'h') and pieces['right']:
                        self._slide(pieces['right'], pieces['center'],
                                    (-self.piece_size, 0))
                    if event.keysym in ('Right', 'l') and pieces['left']:
                        self._slide(pieces['left'], pieces['center'],
                                    (self.piece_size, 0))
                    self.check_status()

                def _slide(self, from_, to, coord):
                    self.canvas.move(from_['id'], *coord)
                    to['pos_a'], from_['pos_a'] = from_['pos_a'], to['pos_a']
                    self.steps += 1

                def get_pieces_around(self):
                    pieces = {'center': None,
                              'right' : None,
                              'left'  : None,
                              'top'   : None,
                              'bottom': None}
                    for piece in self.board:
                        if not piece['visible']:
                            pieces['center'] = piece
                            break
                    x0, y0 = pieces['center']['pos_a']
                    for piece in self.board:
                        x1, y1 = piece['pos_a']
                        if y0 == y1 and x1 == x0 + 1:
                            pieces['right'] = piece
                        if y0 == y1 and x1 == x0 - 1:
                            pieces['left'] = piece
                        if x0 == x1 and y1 == y0 - 1:
                            pieces['top'] = piece
                        if x0 == x1 and y1 == y0 + 1:
                            pieces['bottom'] = piece
                    return pieces

                def create_board(self):
                    self.board = []
                    for x in range(self.board_grid):
                        for y in range(self.board_grid):
                            x0 = x * self.piece_size
                            y0 = y * self.piece_size
                            x1 = x0 + self.piece_size
                            y1 = y0 + self.piece_size
                            image = ImageTk.PhotoImage(
                                    self.image.crop((x0, y0, x1, y1)))
                            piece = {'id'     : None,
                                     'image'  : image,
                                     'pos_o'  : (x, y),
                                     'pos_a'  : None,
                                     'visible': True}
                            self.board.append(piece)
                    self.board[-1]['visible'] = False

                def check_status(self):
                    for piece in self.board:
                        if piece['pos_a'] != piece['pos_o']:
                            return
                    title = 'Ganaste!'
                    message = 'Lo resolviste en %d movidas!' % self.steps
                    tkMessageBox.showinfo(title, message)

                def show(self):
                    random.shuffle(self.board)
                    index = 0
                    for x in range(self.board_grid):
                        for y in range(self.board_grid):
                            self.board[index]['pos_a'] = (x, y)
                            if self.board[index]['visible']:
                                x1 = x * self.piece_size
                                y1 = y * self.piece_size
                                image = self.board[index]['image']
                                id = self.canvas.create_image(
                                        x1, y1, image=image, anchor=tk.NW)
                                self.board[index]['id'] = id
                            index += 1


            if __name__ == '__main__':
                from optparse import OptionParser
                parser = OptionParser(description="Sliding puzzle")
                parser.add_option('-g', '--board-grid', type=int, default=4,
                                  help="(the minimum value is 3)")
                parser.add_option('-i', '--image', type=str, default=a,
                                  help="path to image")
                args, _ = parser.parse_args()

                if args.board_grid < 3:
                    args.board_grid = 3
                    print("Warning: using 3 for board-grid")

                app = Application(args.image, args.board_grid)
                app.master.title('Sliding puzzle')
                app.mainloop()

            #from Options import kingss
            #kingss.main()



























                
        elif args == 2:
                import random
                import tkinter as tk
                import tkinter.messagebox
                from PIL import Image, ImageTk
                import random
                #tk.geometry(1000x1000)
                MAX_BOARD_SIZE = 600
                files=['pic_1.jpeg','pic_3.jpeg','pic_5.jpeg']
                a=random.choice(files)
                class Application(tk.Frame):

                    def __init__(self, image, board_grid=4):
                        tk.Frame.__init__(self)
                        self.grid()
                        self.board_grid = board_grid if board_grid > 2 else 3
                        self.load_image(image)
                        self.steps = 0
                        self.create_widgets()
                        self.create_events()
                        self.create_board()
                        self.show()

                    def load_image(self, image):
                        image = Image.open(image)
                        board_size = min(image.size)
                        if image.size[0] != image.size[1]:
                            image = image.crop((0, 0, board_size, board_size))
                        if board_size > MAX_BOARD_SIZE:
                            board_size = MAX_BOARD_SIZE
                            image = image.resize((board_size, board_size), Image.ANTIALIAS)
                        self.image = image
                        self.board_size = board_size
                        self.piece_size = self.board_size / self.board_grid

                    def create_widgets(self):
                        args = dict(width=self.board_size, height=self.board_size)
                        self.canvas = tk.Canvas(self, **args)
                        self.canvas.grid(row=0,column=0)
                        
                        #self.canvas = tk.Canvas(width=300, height=300, bg='white')
                        #self.canvas.grid()

                        load = Image.open(a)
                        render = ImageTk.PhotoImage(load)
                        
                        widget = tk.Label(self, image=render, fg='white', bg='black')
                        widget.image = render
                        widget.place(x=0,y=0)
                        widget.grid(row=0,column=1)
                        #self.canvas.create_window(100, 100, window=widget)

                    def create_events(self):
                        self.canvas.bind_all('<KeyPress-Up>', self.slide)
                        self.canvas.bind_all('<KeyPress-Down>', self.slide)
                        self.canvas.bind_all('<KeyPress-Left>', self.slide)
                        self.canvas.bind_all('<KeyPress-Right>', self.slide)
                        self.canvas.bind_all('<KeyPress-h>', self.slide)
                        self.canvas.bind_all('<KeyPress-j>', self.slide)
                        self.canvas.bind_all('<KeyPress-k>', self.slide)
                        self.canvas.bind_all('<KeyPress-l>', self.slide)
                        self.canvas.bind_all('<KeyPress-H>', self.help)

                    def help(self, event):
                        if getattr(self, '_img_help_id', None) is None:
                            self._img_help = ImageTk.PhotoImage(self.image)
                            self._img_help_id = self.canvas.create_image(0, 0,
                                    image=self._img_help, anchor=tk.NW)
                        else:
                            state = self.canvas.itemcget(self._img_help_id, 'state')
                            state = 'hidden' if state == '' else ''
                            self.canvas.itemconfigure(self._img_help_id, state=state)

                    def slide(self, event):
                        pieces = self.get_pieces_around()
                        if event.keysym in ('Up', 'k') and pieces['bottom']:
                            self._slide(pieces['bottom'], pieces['center'], 
                                        (0, -self.piece_size))
                        if event.keysym in ('Down', 'j') and pieces['top']:
                            self._slide(pieces['top'], pieces['center'],
                                        (0, self.piece_size))
                        if event.keysym in ('Left', 'h') and pieces['right']:
                            self._slide(pieces['right'], pieces['center'],
                                        (-self.piece_size, 0))
                        if event.keysym in ('Right', 'l') and pieces['left']:
                            self._slide(pieces['left'], pieces['center'],
                                        (self.piece_size, 0))
                        self.check_status()

                    def _slide(self, from_, to, coord):
                        self.canvas.move(from_['id'], *coord)
                        to['pos_a'], from_['pos_a'] = from_['pos_a'], to['pos_a']
                        self.steps += 1

                    def get_pieces_around(self):
                        pieces = {'center': None,
                                  'right' : None,
                                  'left'  : None,
                                  'top'   : None,
                                  'bottom': None}
                        for piece in self.board:
                            if not piece['visible']:
                                pieces['center'] = piece
                                break
                        x0, y0 = pieces['center']['pos_a']
                        for piece in self.board:
                            x1, y1 = piece['pos_a']
                            if y0 == y1 and x1 == x0 + 1:
                                pieces['right'] = piece
                            if y0 == y1 and x1 == x0 - 1:
                                pieces['left'] = piece
                            if x0 == x1 and y1 == y0 - 1:
                                pieces['top'] = piece
                            if x0 == x1 and y1 == y0 + 1:
                                pieces['bottom'] = piece
                        return pieces

                    def create_board(self):
                        self.board = []
                        for x in range(self.board_grid):
                            for y in range(self.board_grid):
                                x0 = x * self.piece_size
                                y0 = y * self.piece_size
                                x1 = x0 + self.piece_size
                                y1 = y0 + self.piece_size
                                image = ImageTk.PhotoImage(
                                        self.image.crop((x0, y0, x1, y1)))
                                piece = {'id'     : None,
                                         'image'  : image,
                                         'pos_o'  : (x, y),
                                         'pos_a'  : None,
                                         'visible': True}
                                self.board.append(piece)
                        self.board[-1]['visible'] = False

                    def check_status(self):
                        for piece in self.board:
                            if piece['pos_a'] != piece['pos_o']:
                                return
                        title = 'Ganaste!'
                        message = 'Lo resolviste en %d movidas!' % self.steps
                        tkMessageBox.showinfo(title, message)

                    def show(self):
                        random.shuffle(self.board)
                        index = 0
                        for x in range(self.board_grid):
                            for y in range(self.board_grid):
                                self.board[index]['pos_a'] = (x, y)
                                if self.board[index]['visible']:
                                    x1 = x * self.piece_size
                                    y1 = y * self.piece_size
                                    image = self.board[index]['image']
                                    id = self.canvas.create_image(
                                            x1, y1, image=image, anchor=tk.NW)
                                    self.board[index]['id'] = id
                                index += 1


                if __name__ == '__main__':
                    from optparse import OptionParser
                    parser = OptionParser(description="Sliding puzzle")
                    parser.add_option('-g', '--board-grid', type=int, default=4,
                                      help="(the minimum value is 3)")
                    parser.add_option('-i', '--image', type=str, default=a,
                                      help="path to image")
                    args, _ = parser.parse_args()

                    if args.board_grid < 3:
                        args.board_grid = 3
                        print("Warning: using 3 for board-grid")

                    app = Application(args.image, args.board_grid)
                    app.master.title('Sliding puzzle')
                    app.mainloop()

            #from Options import kingss
            #kingss.main()




##            from Options import Body_parts
##            Body_parts.main()







































                
        elif args == 3:
                import random
                import tkinter as tk
                import tkinter.messagebox
                from PIL import Image, ImageTk
                import random
                #tk.geometry(1000x1000)
                MAX_BOARD_SIZE = 600
                files=['s_2.jpeg','s_1.jpeg','s_3.jpeg','s_4.jpeg','s_5.jpeg',]
                a=random.choice(files)
                class Application(tk.Frame):

                    def __init__(self, image, board_grid=4):
                        tk.Frame.__init__(self)
                        self.grid()
                        self.board_grid = board_grid if board_grid > 2 else 3
                        self.load_image(image)
                        self.steps = 0
                        self.create_widgets()
                        self.create_events()
                        self.create_board()
                        self.show()

                    def load_image(self, image):
                        image = Image.open(image)
                        board_size = min(image.size)
                        if image.size[0] != image.size[1]:
                            image = image.crop((0, 0, board_size, board_size))
                        if board_size > MAX_BOARD_SIZE:
                            board_size = MAX_BOARD_SIZE
                            image = image.resize((board_size, board_size), Image.ANTIALIAS)
                        self.image = image
                        self.board_size = board_size
                        self.piece_size = self.board_size / self.board_grid

                    def create_widgets(self):
                        args = dict(width=self.board_size, height=self.board_size)
                        self.canvas = tk.Canvas(self, **args)
                        self.canvas.grid(row=0,column=0)
                        
                        #self.canvas = tk.Canvas(width=300, height=300, bg='white')
                        #self.canvas.grid()

                        load = Image.open(a)
                        render = ImageTk.PhotoImage(load)
                        
                        widget = tk.Label(self, image=render, fg='white', bg='black')
                        widget.image = render
                        widget.place(x=0,y=0)
                        widget.grid(row=0,column=1)
                        #self.canvas.create_window(100, 100, window=widget)

                    def create_events(self):
                        self.canvas.bind_all('<KeyPress-Up>', self.slide)
                        self.canvas.bind_all('<KeyPress-Down>', self.slide)
                        self.canvas.bind_all('<KeyPress-Left>', self.slide)
                        self.canvas.bind_all('<KeyPress-Right>', self.slide)
                        self.canvas.bind_all('<KeyPress-h>', self.slide)
                        self.canvas.bind_all('<KeyPress-j>', self.slide)
                        self.canvas.bind_all('<KeyPress-k>', self.slide)
                        self.canvas.bind_all('<KeyPress-l>', self.slide)
                        self.canvas.bind_all('<KeyPress-H>', self.help)

                    def help(self, event):
                        if getattr(self, '_img_help_id', None) is None:
                            self._img_help = ImageTk.PhotoImage(self.image)
                            self._img_help_id = self.canvas.create_image(0, 0,
                                    image=self._img_help, anchor=tk.NW)
                        else:
                            state = self.canvas.itemcget(self._img_help_id, 'state')
                            state = 'hidden' if state == '' else ''
                            self.canvas.itemconfigure(self._img_help_id, state=state)

                    def slide(self, event):
                        pieces = self.get_pieces_around()
                        if event.keysym in ('Up', 'k') and pieces['bottom']:
                            self._slide(pieces['bottom'], pieces['center'], 
                                        (0, -self.piece_size))
                        if event.keysym in ('Down', 'j') and pieces['top']:
                            self._slide(pieces['top'], pieces['center'],
                                        (0, self.piece_size))
                        if event.keysym in ('Left', 'h') and pieces['right']:
                            self._slide(pieces['right'], pieces['center'],
                                        (-self.piece_size, 0))
                        if event.keysym in ('Right', 'l') and pieces['left']:
                            self._slide(pieces['left'], pieces['center'],
                                        (self.piece_size, 0))
                        self.check_status()

                    def _slide(self, from_, to, coord):
                        self.canvas.move(from_['id'], *coord)
                        to['pos_a'], from_['pos_a'] = from_['pos_a'], to['pos_a']
                        self.steps += 1

                    def get_pieces_around(self):
                        pieces = {'center': None,
                                  'right' : None,
                                  'left'  : None,
                                  'top'   : None,
                                  'bottom': None}
                        for piece in self.board:
                            if not piece['visible']:
                                pieces['center'] = piece
                                break
                        x0, y0 = pieces['center']['pos_a']
                        for piece in self.board:
                            x1, y1 = piece['pos_a']
                            if y0 == y1 and x1 == x0 + 1:
                                pieces['right'] = piece
                            if y0 == y1 and x1 == x0 - 1:
                                pieces['left'] = piece
                            if x0 == x1 and y1 == y0 - 1:
                                pieces['top'] = piece
                            if x0 == x1 and y1 == y0 + 1:
                                pieces['bottom'] = piece
                        return pieces

                    def create_board(self):
                        self.board = []
                        for x in range(self.board_grid):
                            for y in range(self.board_grid):
                                x0 = x * self.piece_size
                                y0 = y * self.piece_size
                                x1 = x0 + self.piece_size
                                y1 = y0 + self.piece_size
                                image = ImageTk.PhotoImage(
                                        self.image.crop((x0, y0, x1, y1)))
                                piece = {'id'     : None,
                                         'image'  : image,
                                         'pos_o'  : (x, y),
                                         'pos_a'  : None,
                                         'visible': True}
                                self.board.append(piece)
                        self.board[-1]['visible'] = False

                    def check_status(self):
                        for piece in self.board:
                            if piece['pos_a'] != piece['pos_o']:
                                return
                        title = 'Ganaste!'
                        message = 'Lo resolviste en %d movidas!' % self.steps
                        tkMessageBox.showinfo(title, message)

                    def show(self):
                        random.shuffle(self.board)
                        index = 0
                        for x in range(self.board_grid):
                            for y in range(self.board_grid):
                                self.board[index]['pos_a'] = (x, y)
                                if self.board[index]['visible']:
                                    x1 = x * self.piece_size
                                    y1 = y * self.piece_size
                                    image = self.board[index]['image']
                                    id = self.canvas.create_image(
                                            x1, y1, image=image, anchor=tk.NW)
                                    self.board[index]['id'] = id
                                index += 1


                if __name__ == '__main__':
                    from optparse import OptionParser
                    parser = OptionParser(description="Sliding puzzle")
                    parser.add_option('-g', '--board-grid', type=int, default=4,
                                      help="(the minimum value is 3)")
                    parser.add_option('-i', '--image', type=str, default=a,
                                      help="path to image")
                    args, _ = parser.parse_args()

                    if args.board_grid < 3:
                        args.board_grid = 3
                        print("Warning: using 3 for board-grid")

                    app = Application(args.image, args.board_grid)
                    app.master.title('Sliding puzzle')
                    app.mainloop()

            #from Options import kingss
            #kingss.main()
                    





















































##            from Options import Colour
##            Colour.main()
        elif args == 4:
            
            import random
            import tkinter as tk
            import tkinter.messagebox
            from PIL import Image, ImageTk
            import random
            #tk.geometry(1000x1000)
            MAX_BOARD_SIZE = 600
            files=['sarojini.jpeg','bhagat.jpeg','azad.jpeg','lala.jpeg','subhash.jpeg']
            a=random.choice(files)
            class Application(tk.Frame):

                def __init__(self, image, board_grid=4):
                    tk.Frame.__init__(self)
                    self.grid()
                    self.board_grid = board_grid if board_grid > 2 else 3
                    self.load_image(image)
                    self.steps = 0
                    self.create_widgets()
                    self.create_events()
                    self.create_board()
                    self.show()

                def load_image(self, image):
                    image = Image.open(image)
                    board_size = min(image.size)
                    if image.size[0] != image.size[1]:
                        image = image.crop((0, 0, board_size, board_size))
                    if board_size > MAX_BOARD_SIZE:
                        board_size = MAX_BOARD_SIZE
                        image = image.resize((board_size, board_size), Image.ANTIALIAS)
                    self.image = image
                    self.board_size = board_size
                    self.piece_size = self.board_size / self.board_grid

                def create_widgets(self):
                    args = dict(width=self.board_size, height=self.board_size)
                    self.canvas = tk.Canvas(self, **args)
                    self.canvas.grid(row=0,column=0)
                    
                    #self.canvas = tk.Canvas(width=300, height=300, bg='white')
                    #self.canvas.grid()

                    load = Image.open(a)
                    render = ImageTk.PhotoImage(load)
                    
                    widget = tk.Label(self, image=render, fg='white', bg='black')
                    widget.image = render
                    widget.place(x=0,y=0)
                    widget.grid(row=0,column=1)
                    #self.canvas.create_window(100, 100, window=widget)

                def create_events(self):
                    self.canvas.bind_all('<KeyPress-Up>', self.slide)
                    self.canvas.bind_all('<KeyPress-Down>', self.slide)
                    self.canvas.bind_all('<KeyPress-Left>', self.slide)
                    self.canvas.bind_all('<KeyPress-Right>', self.slide)
                    self.canvas.bind_all('<KeyPress-h>', self.slide)
                    self.canvas.bind_all('<KeyPress-j>', self.slide)
                    self.canvas.bind_all('<KeyPress-k>', self.slide)
                    self.canvas.bind_all('<KeyPress-l>', self.slide)
                    self.canvas.bind_all('<KeyPress-H>', self.help)

                def help(self, event):
                    if getattr(self, '_img_help_id', None) is None:
                        self._img_help = ImageTk.PhotoImage(self.image)
                        self._img_help_id = self.canvas.create_image(0, 0,
                                image=self._img_help, anchor=tk.NW)
                    else:
                        state = self.canvas.itemcget(self._img_help_id, 'state')
                        state = 'hidden' if state == '' else ''
                        self.canvas.itemconfigure(self._img_help_id, state=state)

                def slide(self, event):
                    pieces = self.get_pieces_around()
                    if event.keysym in ('Up', 'k') and pieces['bottom']:
                        self._slide(pieces['bottom'], pieces['center'], 
                                    (0, -self.piece_size))
                    if event.keysym in ('Down', 'j') and pieces['top']:
                        self._slide(pieces['top'], pieces['center'],
                                    (0, self.piece_size))
                    if event.keysym in ('Left', 'h') and pieces['right']:
                        self._slide(pieces['right'], pieces['center'],
                                    (-self.piece_size, 0))
                    if event.keysym in ('Right', 'l') and pieces['left']:
                        self._slide(pieces['left'], pieces['center'],
                                    (self.piece_size, 0))
                    self.check_status()

                def _slide(self, from_, to, coord):
                    self.canvas.move(from_['id'], *coord)
                    to['pos_a'], from_['pos_a'] = from_['pos_a'], to['pos_a']
                    self.steps += 1

                def get_pieces_around(self):
                    pieces = {'center': None,
                              'right' : None,
                              'left'  : None,
                              'top'   : None,
                              'bottom': None}
                    for piece in self.board:
                        if not piece['visible']:
                            pieces['center'] = piece
                            break
                    x0, y0 = pieces['center']['pos_a']
                    for piece in self.board:
                        x1, y1 = piece['pos_a']
                        if y0 == y1 and x1 == x0 + 1:
                            pieces['right'] = piece
                        if y0 == y1 and x1 == x0 - 1:
                            pieces['left'] = piece
                        if x0 == x1 and y1 == y0 - 1:
                            pieces['top'] = piece
                        if x0 == x1 and y1 == y0 + 1:
                            pieces['bottom'] = piece
                    return pieces

                def create_board(self):
                    self.board = []
                    for x in range(self.board_grid):
                        for y in range(self.board_grid):
                            x0 = x * self.piece_size
                            y0 = y * self.piece_size
                            x1 = x0 + self.piece_size
                            y1 = y0 + self.piece_size
                            image = ImageTk.PhotoImage(
                                    self.image.crop((x0, y0, x1, y1)))
                            piece = {'id'     : None,
                                     'image'  : image,
                                     'pos_o'  : (x, y),
                                     'pos_a'  : None,
                                     'visible': True}
                            self.board.append(piece)
                    self.board[-1]['visible'] = False

                def check_status(self):
                    for piece in self.board:
                        if piece['pos_a'] != piece['pos_o']:
                            return
                    title = 'Ganaste!'
                    message = 'Lo resolviste en %d movidas!' % self.steps
                    tkMessageBox.showinfo(title, message)

                def show(self):
                    random.shuffle(self.board)
                    index = 0
                    for x in range(self.board_grid):
                        for y in range(self.board_grid):
                            self.board[index]['pos_a'] = (x, y)
                            if self.board[index]['visible']:
                                x1 = x * self.piece_size
                                y1 = y * self.piece_size
                                image = self.board[index]['image']
                                id = self.canvas.create_image(
                                        x1, y1, image=image, anchor=tk.NW)
                                self.board[index]['id'] = id
                            index += 1


            if __name__ == '__main__':
                from optparse import OptionParser
                parser = OptionParser(description="Sliding puzzle")
                parser.add_option('-g', '--board-grid', type=int, default=4,
                                  help="(the minimum value is 3)")
                parser.add_option('-i', '--image', type=str, default=a,
                                  help="path to image")
                args, _ = parser.parse_args()

                if args.board_grid < 3:
                    args.board_grid = 3
                    print("Warning: using 3 for board-grid")

                app = Application(args.image, args.board_grid)
                app.master.title('Sliding puzzle')
                app.mainloop()









































                
##            from Options import Fruit
##            Fruit.main()
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
            bg='#FF69B4',
            border=0,
            justify='center',

        )
        sel_btn1 = Button(
            text="National symbols",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#DDA0DD",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Historical rulers",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#DDA0DD",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="monuments",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#DDA0DD",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Freedom fighters",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#DDA0DD",
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
        sel_btn1.grid(row=1, column=1, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=2, column=1, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=3, column=1, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=4, column=1, pady=(10, 0), padx=50, )
        #sel_btn5.grid(row=5, column=1, pady=(10, 0), padx=50, )
        #sel_btn1.grid(row=6, column=1, pady=(10, 0), padx=50, )
        #sel_btn7.grid(row=6, column=1, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+400+100")
    main_window.resizable(0, 0)
    main_window.title("PUZZLE MANIA")
    main_window.configure(background="#FF69B4")
    #main_window.iconbitmap(r'quizee_logo_.ico')

    img0 = PhotoImage(file="puzzle_cover.png")
    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        image=img0,
        bg='#FF69B4',
    )
    lab_img.pack(pady=(45, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#DDA0DD",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(40, 20))

    main_window.mainloop()


start_main_page()
