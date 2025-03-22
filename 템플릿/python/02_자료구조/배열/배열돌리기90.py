import sys
from pprint import pprint

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
board2 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
# 90도 돌리기


def rotate90(board):
    Y = len(board)
    X = len(board[0])
    return [[board[~y][x] for y in range(Y)] for x in range(X)]

# 180도 돌리기


def rotate180(y, board):
    Y = len(board)
    X = len(board[0])
    return [[board[~y][~x] for x in range(X)] for y in range(Y)]

# 270도 돌리기


def rotate270(y, board):
    Y = len(board)
    X = len(board[0])
    return [[board[y][~x] for y in range(Y)] for x in range(X)]

# 프린트


def Print(board):
    return list(map(lambda a: print(*a), board))


Print(rotate90(board))
print('---')
Print(rotate180(1, board))
print('---')
Print(rotate270(1, board))
print('---')
Print(rotate90(board2))
print('---')
Print(rotate180(1, board2))
print('---')
Print(rotate270(1, board2))
print('---')
