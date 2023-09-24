from board import *

def main():
    board = ChessBoard()
    board.move_piece("e2", "e4")
    print(board)
    board.move_piece("e7", "e5")
    print(board)
    board.move_piece("g1", "f3")
    print(board)
    board.move_piece("b8", "c6")
    print(board)
    board.move_piece("f1", "c4")
    print(board)
    board.move_piece("d8", "h4")
    print(board)
    board.move_piece("f3", "h4")
    print(board)

if __name__ == "__main__":
    main()