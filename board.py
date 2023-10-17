from pieces import *
from utils import *

class ChessBoard:
    """
    ChessBoard object representing a chessboard, using a nested list containing
    either a Piece or None.
    """

    def __init__(self):
        # Nested lists are y-axis, outside list is x-axis
        # Reference square e4 with board[4][3]
        self.board = [[None] * BOARD_HEIGHT for i in range(BOARD_LENGTH)]
        self.__load_pawns()
        self.__load_pieces("w")
        self.__load_pieces("b")

    def __load_pawns(self) -> None:
        """Helper funtion for __init__ which generates and places pawns."""

        for i in range(BOARD_LENGTH):
            self.board[i][W_PAWN_ROW] = Pawn("w")
            self.board[i][B_PAWN_ROW] = Pawn("b")

    def __load_pieces(self, colour: str) -> None:
        """
        Helper function for __init__ which generates and places non pawn
        pieces.
        
        Args:
            colour: colour of the pieces to be placed
        """

        row = W_PIECE_ROW
        if colour == "b":
            row = B_PIECE_ROW

        # Dictionary of pieces and their columns on the board
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

        # Placing pieces on the board, using numeric indexes
        for key, value in pieces.items():
            self.board[key][row] = value

    def __str__(self) -> str:
        """
        Returns graphic representation of the board using characters. White
        pieces are uppercase, black pieces are lowercase.
        """

        # String builder
        sb = ""

        for i in reversed(range(BOARD_HEIGHT)):

            # Row number and spacing
            sb += str(i + 1) + "  "

            for j in range(BOARD_LENGTH):
                # Piece representations, with # for empty squares
                if self.board[j][i] == None:
                    sb += "# "
                else:
                    sb += str(self.board[j][i]) + " "
            sb += "\n"

        # Column names
        sb += "\n   "
        for i in range(ord("a"), ord("h") + 1):
            sb += chr(i) + " "

        # Extra new lines for visibility when printed in sequence
        sb += "\n\n"

        return sb

    def place_piece(self, piece: ChessPiece, pos: str) -> None:
        """
        Places a piece on a square on the board.

        Args:
            piece: piece object to be placed
            pos: string representation of target square
        """

        x, y = position_numeric(pos)
        self.board[x][y] = piece

    def fetch_piece(self, pos: str) -> ChessPiece:
        """
        Returns the piece object on the specified square on the board.

        Args:
            pos: string representation of target square
        """

        x, y = position_numeric(pos)
        return self.board[x][y]

    # Parses a move from algebraic notation and enacts it
    def parse_move(self, move: str):
        # Castling
        if move == "0-0":
            self.move_piece("e1", "g1")
            self.move_piece("h1", "f1")
                

        elif move == "0-0-0":
            self.move_piece("e1", "c1")
            self.move_piece("a1", "d1")

        # Checkmate
        elif move[-1] == "#":
            self.parse_move(move[:-1])
            print("Checkmate!")

        #Check
        elif move[-1] == "+":
            self.parse_move(move[:-1])
            print("Check!")

        # Capture
        elif "x" in move:
            if move[0].islower():
                # Find pawn location
                self.move_piece("pawn_location", move[2:])
            else:
                self.parse_move(move[0] + move[2:])
                
        # Two pieces move to same square
        
        # Two pieces move to same square and same column
        
        # Normal case
        else:
            piece = move[0]
            there = move[1:]
            self.move_piece("here_location", there)
    
    # Moves a piece from square 'here' to 'there'
    def move_piece(self, here: str, there: str):
        piece = self.fetch_piece(here)
        if piece == None:
            return False        
        if there in piece.valid_moves(self.board, here):
            self.place_piece(piece, there)
            self.place_piece(None, here)
            return True
        else:
            return False
