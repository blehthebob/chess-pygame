class ChessPiece:
    def __init__(self, colour: str):
        self.symbol: str = None
        self.colour: str = colour
    
    def can_move():
        pass
    
    def __str__(self):
        if self.colour == "w":
            return self.symbol
        else:
            return self.symbol.lower()
    
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
        
class Pawn(ChessPiece):
    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = "P"