import sys
from collections import deque
sys.stdin = open("16927.txt", "r")
input = sys.stdin.readline
Y, X, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
_board = [[0] * X for _ in range(Y)]
di = ((1, 0), (0, 1), (-1, 0), (0, -1))
sX, eX = 0, X
sY, eY = 0, Y
while sX < eX and sY < eY:
    values = deque([])
    points = deque([])
    y, x = sY, sX
    for dy, dx in di:
        while True:
            if sX <= x + dx < eX and sY <= y + dy < eY:
                points.append((y, x))
                values.append(board[y][x])
                y += dy
                x += dx
            else:
                break
    sX += 1
    sY += 1
    eX -= 1
    eY -= 1
    values.rotate(R)
    for i in range(len(points)):
        ny, nx = points[i]
        value = values[i]
        _board[ny][nx] = value
        
list(map(lambda a: print(*a), _board))
