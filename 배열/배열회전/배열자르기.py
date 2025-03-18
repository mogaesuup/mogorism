import sys
from pprint import pprint

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# y기준 자르기


def sliceY(y, board):
    Y = len(board)
    X = len(board[0])
    return [board[y][x] for x in range(X)]

# x기준 자르기


def sliceX(x, board):
    Y = len(board)
    X = len(board[0])
    return [board[y][x] for y in range(Y)]


print(sliceX(1, board))
print(sliceY(1, board))
