from pieces import *
from utils import *

class ChessBoard:
    def __init__(self):
        # Nested lists are y-axis, outside list is x-axis
        # Reference square e4 with board[4][3]
        self.board = [[None] * BOARD_HEIGHT for i in range(BOARD_LENGTH)]
        self.load_pawns()
        self.load_pieces("w")
        self.load_pieces("b")
        
    # Generate and place pawns
    def load_pawns(self):
        for i in range(BOARD_LENGTH):
            self.board[i][PAWN_ROW] = Pawn("w")
            self.board[i][BOARD_HEIGHT - PAWN_ROW - 1] = Pawn("b")
    
    def load_pieces(self, colour):
        row = PIECE_ROW
        if colour == "b":
            row = BOARD_HEIGHT - PIECE_ROW - 1
        
        pieces = {
            0: Rook(colour),
            1: Knight(colour),
            2: Bishop(colour),
            3: Queen(colour),
            4: King(colour),
            5: Bishop(colour),
            6: Knight(colour),
            7: Rook(colour)
        }
        
        for key, value in pieces.items():
            self.board[key][row] = value
    
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