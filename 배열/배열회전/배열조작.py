import sys
from pprint import pprint

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
y = 1
x = 1
#  -1,-1   -1, 0    -1,1
#   0,-1    0, 0     0,1
#   1,-1    1, 0     1,1
di = [(-1, -1), (-1, 0), (-1, 1),
      (0, -1), (0, 0), (0, 1),
      (1, -1), (1, 0), (1, 1)]
# 북서 -1, -1
ny, nx = y + di[0][0], x + di[0][1]
print(board[ny][nx])
# 위 -1, 0
ny, nx = y + di[1][0], x + di[1][1]
print(board[ny][nx])
# 북동 -1, 1
ny, nx = y + di[2][0], x + di[2][1]
print(board[ny][nx])
# 서 0, -1
ny, nx = y + di[3][0], x + di[3][1]
print(board[ny][nx])
# 가운데 0, 0
ny, nx = y + di[4][0], x + di[4][1]
print(board[ny][nx])
# 동 0, 1
ny, nx = y + di[5][0], x + di[5][1]
print(board[ny][nx])
# 남서 1, -1
ny, nx = y + di[6][0], x + di[6][1]
print(board[ny][nx])
# 아래 1, 0
ny, nx = y + di[7][0], x + di[7][1]
print(board[ny][nx])
# 남동 1, 1
ny, nx = y + di[8][0], x + di[8][1]
print(board[ny][nx])
