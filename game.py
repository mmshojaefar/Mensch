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

    def start(self):
        self.sort_turns()
        # player_turn = None
        for p in self.players:
            if p.color == self.turn:
                player_turn = p

        iter = 0
        while self.turns:
            iter += 1
            print()
            print('------------------------')
            print(player_turn.board)
            dice = player_turn.dice()
            print(f'turn: {self.turn}, dice: {dice}')
            n = 0
            if player_turn.can_move:
                print([(player_turn.can_move[i].real_location,player_turn.can_move[i].color) for i in range(len(player_turn.can_move))])
                n = int(input())
            player_turn.select(n, dice)

            for p in self.players:
                print(p.remain_piece, p.piece_in_game, p.piece_in_home, end=' / ')
            
            if dice != 6:
                player_turn = self.next(player_turn)
                self.turn = player_turn.color
        print('')
        print('**********************')
        print(f'game ends in {iter}')
        print(self.winner)
        print('**********************')



g = Game(24)
g.add_player('blue')
g.add_player('yellow')
g.add_player('red')
g.start()

#-------------------
# board = 24*[0]
# print(board)
# turn = None
# turns = []
# all = []
# p1 = player('blue', board)
# p2 = player('red', board)
# p = []
# print(turns)
# print(player.turn)
# p.append(p1)
# p.append(p2)
# pi = p1


# for i in range(1000):
    # print('-----------------')
    # pturn = None
    # for pi in p:
    #     if pi.color == pi.turn:
    #         pturn = pi
    # print(pi.board)
    # dice = pi.dice()
    # n = 0
    # if pi.can_move:
    #     print([(pi.can_move[i].real_location,pi.can_move[i].color) for i in range(len(pi.can_move))])
    #     n = int(input())
    # pi.select(n, dice)
    # print(p1.remain_piece, p1.piece_in_game, p1.piece_in_home)
    # print(p2.remain_piece, p2.piece_in_game, p2.piece_in_home)
    # if dice != 6 and pi == p1:
    #     pi = p2
    # elif dice !=6 and pi == p2:
    #     pi = p1
    # print(pi.can_move)
    # print([pi.can_move[i].real_location for i in range(len(pi.can_move))])

    #vaghti enter mishe, bayad khoneye 0 khali bashe//sample 3 ta adade mokhtale mide
    #list board ro None knm be jaye sefr, harja too shat ham baray board 0 neveshtam, None knm