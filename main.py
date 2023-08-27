from board import *

def main():
    piece = King()
    board = ChessBoard()
    board.place_piece(piece, "e3")
    print(board)

if __name__ == "__main__":
    main()