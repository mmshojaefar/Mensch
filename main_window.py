from tkinter import *
import tkinter.ttk
from first_window import First_Window
from functools import partial
from game import Game
from player import Player
from piece import Piece

class Main_Window:
    def __init__(self, colors_list, mensch, usr):
        self.mensch = mensch
        self.colors = colors_list
        self.last = 1
        self.first_user = usr
        self.names = {}
        self.move_flag = False
        self.dice_number = 1
        self.turn = ''
        # self.num_of_players = len(self.colors)
        self.winners = dict()

        self.root = Tk()
        self.root.title('Mensch')
        self.root.resizable(0, 0)

        # create a toplevel menu
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0, background='white')
        self.filemenu.add_command(label="Add Player      ", command=self.add_player)
        self.filemenu.add_command(label="Start Game      ", command=self.start_game)
        self.filemenu.add_command(label="New Game        ", command=self.new_game)
        self.filemenu.add_separator()
        # self.filemenu.add_command(label="Exit        ", command=self.root.quit())
        self.filemenu.add_command(label="Exit        ", command=self.root.destroy)
        self.menubar.add_cascade(label=" Game", menu=self.filemenu)
        self.filemenu.entryconfig(1, state="disabled")

        # display the menu
        self.root.config(menu=self.menubar)

        self.set_font = ("default", 18)

        # display players
        self.players_label = Label(self.root, text = "Players", anchor="center", width=15, font=self.set_font)
        self.players_label.grid(row=0, column=0)

        # display seperator line
        tkinter.ttk.Separator(self.root, orient=VERTICAL).grid(row=0, column=1, rowspan=30, sticky='ns')
        tkinter.ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=1, sticky="ew")

        # display bottom sec
        self.turns_label = Label(self.root, text = "TURN:", anchor="center", font=self.set_font)
        self.turns_label.grid(row=5, column=0)
        self.dice = Button(self.root, text='Roll Dice', bg='white', font=self.set_font, height=1, width=10, command=self.dice_button, state='disabled')
        self.dice.grid(row=6, column=0, sticky='n')
        self.dice_label = Label(self.root, text='', anchor="center", font=("default", 50), border=1)
        self.dice_label.grid(row=7, column=0)
        
        self.i = 0
        self.img = [None]* 32
        self.butts = [None] * 32
        self.grid_circle()

        self.all_buttons = [self.butts[3], self.butts[7], self.butts[11], self.butts[12], self.butts[13], self.butts[17], self.butts[23],
                       self.butts[22], self.butts[21], self.butts[26], self.butts[30], self.butts[29], self.butts[28], self.butts[24],
                       self.butts[20], self.butts[19], self.butts[18], self.butts[14], self.butts[8], self.butts[9], self.butts[10],
                       self.butts[5], self.butts[1], self.butts[2], self.butts[4], self.butts[31], self.butts[27], self.butts[0], self.butts[6],
                       self.butts[16], self.butts[25], self.butts[15]]
        self.all_buttons_grid = [(1,7),(2,7),(3,7),(3,8),(3,9),(4,9),(5,9),(5,8),(5,7),(6,7),(7,7),(7,6),(7,5),(6,5),(5,5),(5,4),(5,3),(4,3),(3,3),
                            (3,4),(3,5),(2,5),(1,5),(1,6),(1,9),(7,9),(7,3),(1,3),(2,6),(4,8),(6,6),(4,4)]
        self.all_buttons_color = ['#5eff5f','white','white','white','white','white','#ffdc68','white','white','white','white','white','#4f5dff',
                             'white','white','white','white','white','#ff565b','white','white','white','white','white','#5eff5f','#ffdc68',
                             '#4f5dff','#ff565b','#5eff5f','#ffdc68','#4f5dff','#ff565b']
        self.game_buttons = self.all_buttons[:24]
        self.game_buttons_grid = self.all_buttons_grid[:24]
        self.remain_buttons_grid = self.all_buttons_grid[24:28]
        self.home_buttons_grid = self.all_buttons_grid[28:]

        self.pbutts = [None]*16
        self.pimg = [None]*16
        self.player_turn = None
        
    def create_first(self):
        self.last = 2
        self.grid_pieces(self.mensch.turns[-1])
        label = Label(self.root, text='1. '+self.first_user , width=15, font=self.set_font, fg=self.mensch.turns[-1], anchor='w')
        label.place(rely = 0.05)
        self.names[self.mensch.turns[-1]] = self.first_user

    def create_circle(self, color, x, y):
        self.img[self.i] = PhotoImage(file=fr"button\{color}.png")
        self.butts[self.i] = Label(self.root, image=self.img[self.i], border=0, width="77", height="77")
        self.butts[self.i].grid(row=x, column=y+1)
        self.i+=1

    def create_pieces(self, color, x, y, j, bgc):
        self.pimg[j] = PhotoImage(file=fr"pieces\{color}.png")
        self.pbutts[j] = Button(self.root, image=self.pimg[j], border=0, bg=bgc, activebackground=bgc, command=partial(self.move, j))
        self.pbutts[j].grid(row=x, column=y)

    def grid_circle(self):
        # row1
        self.create_circle('red', 1, 2)
        self.create_circle('white', 1, 4)
        self.create_circle('white', 1, 5)
        self.create_circle('green', 1, 6)
        self.create_circle('green', 1, 8)

        # row2
        self.create_circle('white', 2, 4)
        self.create_circle('green', 2, 5)
        self.create_circle('white', 2, 6)

        # row3
        self.create_circle('red', 3, 2)
        self.create_circle('white', 3, 3)
        self.create_circle('white', 3, 4)
        self.create_circle('white', 3, 6)
        self.create_circle('white', 3, 7)
        self.create_circle('white', 3, 8)

        # row4
        self.create_circle('white', 4, 2)
        self.create_circle('red', 4, 3)
        self.create_circle('yellow', 4, 7)
        self.create_circle('white', 4, 8)

        # row5
        self.create_circle('white', 5, 2)
        self.create_circle('white', 5, 3)
        self.create_circle('white', 5, 4)
        self.create_circle('white', 5, 6)
        self.create_circle('white', 5, 7)
        self.create_circle('yellow', 5, 8)

        # row6
        self.create_circle('white', 6, 4)
        self.create_circle('blue', 6, 5)
        self.create_circle('white', 6, 6)

        # row7
        self.create_circle('blue', 7, 2)
        self.create_circle('blue', 7, 4)
        self.create_circle('white', 7, 5)
        self.create_circle('white', 7, 6)
        self.create_circle('yellow', 7, 8)

        # margin
        mar1 = Label(self.root, text = '        ')
        mar2 = Label(self.root, text = '        ')
        mar1.grid(row=8, column=2)
        mar2.grid(row=8, column=10)

    def grid_pieces(self, clr):
        place = {
            'green': (1,9),
            'yellow': (7,9),
            'blue': (7,3),
            'red': (1,3)
        }
        pos = {
            'green': 0,
            'yellow': 4,
            'blue': 8,
            'red': 12
        }
        bgc = {
            'green': '#5eff5f',
            'yellow': '#ffdc68',
            'blue': '#4f5dff',
            'red': '#ff565b'
        }
        for counter in range(4):
            self.create_pieces(clr, place[clr][0], place[clr][1], pos[clr]+counter, bgc[clr] )

    def start_game(self):
        self.num_of_players = len(self.colors)
        self.filemenu.entryconfig(0, state="disabled")
        self.filemenu.entryconfig(1, state="disabled")
        self.dice['state'] = 'normal'
        self.mensch.sort_turns()
        new_names = {}
        for clr in self.mensch.turns:
            new_names[clr] = self.names[clr]
        self.names = new_names.copy()
        self.turns_label['text'] = 'TURN: ' + self.names[list(self.names.keys())[0]]
        self.turns_label['fg'] = list(self.names.keys())[0]
        self.turn = self.mensch.turns[0]
        for p in self.mensch.players:
                if p.color == self.mensch.turn:
                    self.player_turn = p
            
    def add_player(self):
        prevlen = len(self.colors)
        obj = First_Window(self.colors, self.mensch, list(self.names.values()) )
        if len(self.colors) < prevlen:
            self.grid_pieces(self.mensch.turns[-1])
            self.mensch.add_player(self.mensch.turns[-1])
            label = Label(self.root, text=str(self.last)+'. '+obj.usr , width=15, font=self.set_font, fg=self.mensch.turns[-1], anchor='w')
            self.names[self.mensch.turns[-1]] = obj.usr
            label.place(rely=self.last*0.05)
            self.last += 1
            if self.last == 5:
                self.filemenu.entryconfig(0, state="disabled")
            if self.last > 2:
                self.filemenu.entryconfig(1, state="normal")
    
    def new_game(self):
        self.root.destroy()
        # mensch = Game(24)
        # self.__init__(['green','yellow','blue','red'], mensch, '')
        # self.names = {}
        mensch = Game(24)
        colors = ['green', 'yellow', 'blue', 'red']
        obj = First_Window(colors, mensch, [])
        if len(colors) == 3:
            mensch.sort_turns()
            mw = Main_Window(colors, mensch, obj.usr)
            mw.create_first()
            mw.root.mainloop()
        
    def move(self, j):
        print(self.turn, self.player_turn.remain_piece, self.player_turn.piece_in_game, self.player_turn.piece_in_home)
        clr = ['green','yellow','blue','red']
        if self.move_flag and j < clr.index(self.turn)*4+4 and j >= clr.index(self.turn)*4:
            row = self.pbutts[j].grid_info()['row']
            column = self.pbutts[j].grid_info()['column']
            index = self.all_buttons_grid.index((row,column))
            for m in self.player_turn.can_move:
                if self.dice_number == 6 and 24 <= index and index < 28 and m.real_location == -1 and (row,column) in self.remain_buttons_grid:
                    self.move_flag = False
                    x,y = self.all_buttons_grid[m.start_location]
                    self.hit(x,y)
                    self.pbutts[j]['bg'] = self.all_buttons_color[m.start_location]
                    self.pbutts[j]['activebackground'] = self.all_buttons_color[m.start_location]
                    self.pbutts[j].grid(row=x, column=y)
                    m.enter()
                elif index < 24 and m.location + self.dice_number == 24 + m.start_location and m.real_location == index:
                    self.move_flag = False
                    x,y = self.home_buttons_grid[ clr.index(self.mensch.turn) ]
                    self.pbutts[j]['bg'] = self.all_buttons_color[ 28+clr.index(self.mensch.turn) ]
                    self.pbutts[j]['activebackground'] = self.all_buttons_color[ 28+clr.index(self.mensch.turn) ]
                    self.pbutts[j].grid(row=x, column=y)
                    m.move(self.dice_number)
                    print(self.winners)
                    if len(self.player_turn.piece_in_home) == 4:
                        self.winners[self.turn] = self.names[self.turn]
                        if len(self.mensch.turns) == 1:
                            self.move_flag = False
                            self.dice['state'] = 'disabled'
                            # -------------------------
                            self.end_game(self.winners)
                            # end goes here
                            # -------------------------
                            print(self.winners)
                    if len(self.player_turn.piece_in_home) != 0:
                        place = {
                            'green': (2,6),
                            'yellow': (4,8),
                            'blue': (6,6),
                            'red': (4,4)
                        }
                        bgc = {
                            'green': '#277e02',
                            'yellow': '#ffd800',
                            'blue': '#0027fe',
                            'red': '#fe0000'
                        }
                        piece_in_home_label = Label(text=len(self.player_turn.piece_in_home), bg=bgc[self.turn], fg='white')
                        piece_in_home_label.grid(row=place[self.turn][0], column=place[self.turn][1])
                elif index < 24 and m.location + self.dice_number < 24 + m.start_location and m.real_location == index:
                    self.move_flag = False
                    m.move(self.dice_number)
                    x,y = self.game_buttons_grid[ m.real_location]
                    self.hit(x,y)
                    self.pbutts[j]['bg'] = self.all_buttons_color[ m.real_location ]
                    self.pbutts[j]['activebackground'] = self.all_buttons_color[ m.real_location ]
                    self.pbutts[j].grid(row=x, column=y)

            if self.dice_number != 6 and not self.move_flag:
                self.player_turn = self.mensch.next(self.player_turn)
                self.turn = self.player_turn.color
                self.mensch.turn = self.turn
                self.dice_label['text'] = ''
                self.turns_label['fg'] = self.turn
                self.turns_label['text'] = 'TURN: ' + str(self.names[self.turn])
                        
    def dice_button(self):
        if self.move_flag == False:
            self.dice_number = self.player_turn.dice()
            self.dice_label['text'] = str(self.dice_number)
            if self.player_turn.can_move:
                self.move_flag = True
            else:
                self.player_turn = self.mensch.next(self.player_turn)
                self.turn = self.player_turn.color
                self.mensch.turn = self.turn
                self.root.after(500)
                self.dice_label['text'] = ''
                self.turns_label['fg'] = self.player_turn.color        
                self.turns_label['text'] = 'TURN: ' + str(self.names[self.turn])
            print(self.player_turn.color, self.player_turn.can_move)
            
    def hit(self, x ,y):
        for p in self.pbutts:
            if p:
                if p.grid_info()['row'] == x and p.grid_info()['column'] == y:
                    index = int(self.pbutts.index(p)/4)
                    p['bg'] = ['#5eff5f', '#ffdc68', '#4f5dff', '#ff565b'][index]
                    p['activebackground'] = ['#5eff5f', '#ffdc68', '#4f5dff', '#ff565b'][index]
                    p.grid( row = self.remain_buttons_grid[index][0], column = self.remain_buttons_grid[index][1] )

    def end_game(self, rank):
        ranking = Toplevel()
        label0 = Label(ranking, text='')
        label1 = Label(ranking, text='Game Finished!', width=15, font=("default", 17), fg='black')
        label2 = Label(ranking, text='Ranking', width=15, font=("default", 17), fg='black')
        label0.grid(row=0,column=0)
        label1.grid(row=1,column=0)
        label2.grid(row=2,column=0)
        for i in range(len(list(rank.keys()))):
            label = Label(ranking, text=str(i+1) + '.' + rank[list(rank.keys())[i]] , width=15, font=self.set_font, fg=list(rank.keys())[i], anchor='s')
            label.grid(row=i+3,column=0)
        labeln = Label(ranking, text='')
        labeln.grid(row=len(list(rank.keys()))+3,column=0)
        