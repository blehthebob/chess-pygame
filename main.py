from board import *

def main():
    board = ChessBoard()
    board.move_piece("a2", "a4")
    board.move_piece("b7", "b5")
    board.move_piece("a4", "a1")
    board.move_piece("b1", "c3")
    board.move_piece("c3", "c3")
    print(board)

if __name__ == "__main__":
    main()