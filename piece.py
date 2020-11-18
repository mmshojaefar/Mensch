class Piece:
    def __init__(self, color, board, player):
        self.color = color
        self.board = board
        self.player = player
        self.location = -1
        self.real_location = -1
        self.start_location = ['green','yellow','blue','red'].index(color) * 6
        self.circles = 24

    def can_move(self, num):
        if num == 6 and self.real_location == -1:
            return self.can_enter()
        if self.location + num > self.circles + self.start_location:
            return False
        elif self.location + num == self.circles + self.start_location:
            return True
        else:
            if self.board[(self.real_location + num)%self.circles] == None:
                return True
            elif self.board[(self.real_location + num)%self.circles].color == self.color:
                return False
            else:
                return True

    def move(self, num):
        self.board[self.real_location] = None
        self.location += num
        if self.location == self.circles + self.start_location:
            self.player.piece_in_home.append(self)
            self.player.piece_in_game.remove(self)
            self.real_location += num
        else:
            self.real_location = (self.real_location + num) % self.circles
            if self.board[self.real_location] != None:
                self.board[self.real_location].hit()
            self.board[self.real_location] = self
            
    def hit(self):
        self.player.remain_piece.append(self.board[self.real_location])
        self.player.piece_in_game.remove(self.board[self.real_location])
        self.board[self.real_location] = None
        self.location = -1
        self.real_location = -1

    def can_enter(self):
        if self.board[self.start_location] == None:
            return True
        elif self.board[self.start_location].color != self.color:
            return True
        return False
    
    def enter(self):
        self.location = self.start_location
        self.real_location = self.start_location
        if self.board[self.real_location] != None:
            self.board[self.real_location].hit()
        self.board[self.real_location] = self
        self.player.piece_in_game.append(self)
        self.player.remain_piece.remove(self)

    def __repr__(self):
        return f'({self.color}, {self.real_location})'
