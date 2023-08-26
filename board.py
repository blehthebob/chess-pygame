from pieces import *
from utils import *

X_LENGTH = 8
Y_LENGTH = 8

class ChessBoard:
    def __init__(self):
        # Nested lists are y-axis, outside list is x-axis
        # Reference square e4 with board[4][3]
        self.board = [[None] * Y_LENGTH] * X_LENGTH

    # Places a piece on a square on the board.
    def place_piece(self, piece: ChessPiece, pos: str):
        (x, y) = position_numeric(pos)
        self.board[x][y] = piece
    
    # Returns the piece obj on the specified square on the board
    def fetch_piece(self, pos: str):
        (x, y) = position_numeric(pos)
        return self.board[x][y]
    
    # Moves a piece from square 'here' to 'there'
    def move_piece(self, here: str, there: str):
        self.place_piece(self.fetch_piece(here), there)
        self.place_piece(None, here)