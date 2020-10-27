import random
from piece import Piece

class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.piece_in_home = []
        self.piece_in_game = []
        self.remain_piece = [Piece(color,board,self), Piece(color,board,self), Piece(color,board,self), Piece(color,board,self)]
        self.can_move = []

    def dice(self):
        num = random.randint(1,6)
        self.can_move.clear()
        if len(self.piece_in_game) == 0:
            if 6 in [random.randint(1,6), random.randint(1,6), random.randint(1,6)]:
                num = 6
        for p in self.piece_in_game:
            if p.can_move(num):
                self.can_move.append(p)
        if num == 6:
            if self.remain_piece:
                if self.remain_piece[0].can_move(num):
                    self.can_move.append(self.remain_piece[0])
        return num

    def select(self, num, dice):
        if self.can_move:
            if self.can_move[num] in self.remain_piece:
                self.can_move[num].enter()
                self.piece_in_game.append(self.can_move[num])
                self.remain_piece.remove(self.can_move[num])
            else:
                self.can_move[num].move(dice)

    def check_win(self):
        if len(self.piece_in_home) == 4:
            return True
        return False
