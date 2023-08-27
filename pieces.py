from utils import *
from itertools import permutations

class ChessPiece:
    def __init__(self, colour: str):
        self.symbol: str = None
        self.colour: str = colour
    
    # Returns symbol representation of pieces
    # White pieces are upper case and black pieces are lower case
    def __str__(self):
        if self.colour == "w":
            return self.symbol
        else:
            return self.symbol.lower()
        
    # Returns a list of valid moves in notation form given a board in nested
    # list form and the position of the piece
    def valid_moves(self, board, pos: str):
        pass
    
class King(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "K"
        
class Queen(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "Q"
        
class Rook(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "R"
        
class Bishop(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "B"
        
class Knight(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "N"
        
    def valid_moves(self, board, pos: str):
        valid = []
        (x, y) = position_numeric(pos)
        for i, j in list(permutations([-2, -1, 1, 2], 2)):
            if (
                # Check within range of board
                abs(i) + abs(j) == 3 and
                0 <= x + i < BOARD_LENGTH and
                0 <= y + j < BOARD_HEIGHT
            ):
                # Check not own piece
                if board[x + i][y + j] != None:
                    if board[x + i][y + j].colour != self.colour:
                        valid.append(position_notation(x + i, y + j))
                else:
                    valid.append(position_notation(x + i, y + j))
        return valid
        
class Pawn(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "P"
        
    def valid_moves(self, board, pos: str):
        valid = []
        (x, y) = position_numeric(pos)
        
        if self.colour == "w":
            # Move forwards
            if board[x][y + 1] == None:
                valid.append(position_notation(x, y + 1))
                
                # First time moved
                if y == W_PAWN_ROW and board[x][y + 2] == None:
                    valid.append(position_notation(x, y + 2))
                    
            # Take
            if board[x - 1][y + 1] != None and x != 0:
                valid.append(position_notation(x - 1, y + 1))
            if board[x + 1][y + 1] != None and x != BOARD_LENGTH - 1:
                valid.append(position_notation(x + 1, y + 1))
                
            # En passant
            # TODO: do this using a move log?
            
        if self.colour == "b":
            # Move forwards
            if board[x][y - 1] == None:
                valid.append(position_notation(x, y - 1))
                
                # First time moved
                if y == B_PAWN_ROW and board[x][y - 2] == None:
                    valid.append(position_notation(x, y - 2))
                    
            # Take
            if board[x - 1][y - 1] != None and x != 0:
                valid.append(position_notation(x - 1, y - 1))
            if board[x + 1][y - 1] != None and x != BOARD_LENGTH - 1:
                valid.append(position_notation(x + 1, y - 1))
                
            # En passant
            # TODO: do this using a move log?
        return valid