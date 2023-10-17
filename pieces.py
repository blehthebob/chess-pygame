from itertools import permutations
from utils import *

class ChessPiece:
    """
    ChessPiece parent class representing a chess piece. Contains common method
    definitions.
    """

    def __init__(self, colour: str):
        self.symbol: str = None
        self.colour: str = colour

    def __str__(self) -> None:
        """
        Returns symbol representation of pieces.
        White pieces are upper case and black pieces are lower case.
        """

        if self.colour == "w":
            return self.symbol

        return self.symbol.lower()

    def valid_moves(self, board: [list], pos: str) -> [str]:
        """
        Returns a list of valid moves in notation form given a board in nested
        list form and the position of the piece.

        Args:
            board: nested list of either ChessPiece or None elements
            pos: string representation of position of piece
        """

    def check_diagonal(self, board: [list], pos: str) -> [str]:
        """_summary_ # TODO TODO TODO TODO
        ##################################################################
        ###################################################################
        ####################################################################

        Args:
            board: nested list of either ChessPiece or None elements
            pos: string representation of position of piece
        """

        # Function pointers for each direction
        next_square = {
            "nw": lambda x, y: (x - 1, y + 1),
            "ne": lambda x, y: (x + 1, y + 1),
            "sw": lambda x, y: (x - 1, y - 1),
            "se": lambda x, y: (x + 1, y - 1)
        }
        directions = ["nw", "ne", "sw", "se"]
        return self.check_squares(directions, next_square, board, pos)
    
    def check_row(self, board: [list], pos: str) -> [str]:
        """_summary_

        Args:
            board: nested list of either ChessPiece or None elements
            pos: string representation of position of piece
        """

        # Function pointers for each direction
        next_square = {
            "n": lambda x, y: (x, y + 1),
            "e": lambda x, y: (x + 1, y),
            "s": lambda x, y: (x, y - 1),
            "w": lambda x, y: (x - 1, y)
        }
        directions = ["n", "e", "s", "w"]
        return self.check_squares(directions, next_square, board, pos)
    
    # Helper function for check_diagonal and check_row which generalises
    # the checking of valid squares
     # TODO find out what function is
    def check_squares(
        self, directions: [str], next_square, board: [list], pos: str
    ) -> [str]:
        """
        asd

        Args:
            directions (str]): _description_
            next_square (_type_): _description_
            board: nested list of either ChessPiece or None elements
            pos: string representation of position of piece
        """

        valid = []
        for direction in directions:
            (x, y) = position_numeric(pos)
            (x, y) = next_square[direction](x, y)
            while 0 <= x < BOARD_LENGTH and 0 <= y < BOARD_HEIGHT:
                if board[x][y] == None:
                    valid.append(position_notation(x, y))
                elif board[x][y].colour == self.colour:
                    break
                else:
                    valid.append(position_notation(x, y))
                    break
                (x, y) = next_square[direction](x, y)
        return valid
    
class King(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "K"
        
class Queen(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "Q"
    
    def valid_moves(self, board, pos: str):
        valid = super().check_diagonal(board, pos)
        valid += super().check_row(board, pos)
        return valid
        
class Rook(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "R"
    
    def valid_moves(self, board, pos: str):
        return super().check_row(board, pos)
        
class Bishop(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "B"
        
    def valid_moves(self, board, pos: str):
        return super().check_diagonal(board, pos)
    
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