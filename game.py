from player import Player

class Game:
    def __init__(self, circles):
        self.board = circles*[None]
        self.turn = None
        self.turns = []
        self.players = []
        self.winner = []

    def add_player(self, color):        #set number of players later in qt
        self.players.append(Player(color, self.board))
        self.turns.append(color)

    def sort_turns(self):
        temp = []
        for c in ['green', 'yellow', 'blue', 'red']:
            if c in self.turns:
                temp.append(c)
        self.turns = temp
        self.turn = self.turns[0]

    def next(self, player):
        color = player.color
        next_color = self.turns[ (self.turns.index(color) + 1) % len(self.turns) ]
        if player.check_win():
            self.winner.append(player.color)
            self.turns.remove(player.color)
        for p in self.players:
            if p.color == next_color:
                return p
