from board import *

def main():
    board = ChessBoard()
    board.move_piece("a2", "a4")
    board.move_piece("a7", "a5")
    board.move_piece("a4", "a5")
    print(board)

if __name__ == "__main__":
    main()