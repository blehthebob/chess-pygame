from typing import Any
from board import *

class ChessPiece:
    def __init__(self):
        self.symbol = None
        pass
    
    def can_move():
        pass
    
    def __str__(self):
        return self.symbol
    
class King(ChessPiece):
    def __init__(self):
        super().__init__()
        self.symbol = "K"
        
class Queen(ChessPiece):
    def __init__(self):
        super().__init__()
        self.symbol = "Q"
        
class Rook(ChessPiece):
    def __init__(self):
        super().__init__()
        self.symbol = "R"
        
class Bishop(ChessPiece):
    def __init__(self):
        super().__init__()
        self.symbol = "B"
        
class Knight(ChessPiece):
    def __init__(self):
        super().__init__()
        self.symbol = "N"
        
class Pawn(ChessPiece):
    def __init__(self):
        super().__init__()
        self.symbol = "P"