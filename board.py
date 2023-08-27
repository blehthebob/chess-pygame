from pieces import *
from utils import *

BOARD_LENGTH = 8
BOARD_HEIGHT = 8

class ChessBoard:
    def __init__(self):
        # Nested lists are y-axis, outside list is x-axis
        # Reference square e4 with board[4][3]
        self.board = [[None] * BOARD_HEIGHT for i in range(BOARD_LENGTH)]
        
    # Returns graphic representation of the board using characters
    def __str__(self):
        sb = ""
        for i in reversed(range(BOARD_HEIGHT)):
            sb += str(i + 1) + " "
            for j in range(BOARD_LENGTH):
                if self.board[j][i] == None:
                    sb += "# "
                else:
                    sb += str(self.board[j][i]) + " "
            sb += "\n"
        sb += "  "
        for i in range(ord("a"), ord("h") + 1):
            sb += chr(i) + " "
        return sb

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
        piece = self.fetch_piece(here)
        self.place_piece(piece, there)
        self.place_piece(None, here)