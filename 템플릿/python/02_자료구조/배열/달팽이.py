import sys
from collections import deque
from pprint import pprint
sys.stdin = open('10157.txt', 'r')
input = sys.stdin.readline
X, Y = map(int, input().split())
M = int(input())
board = [[0] * X for _ in range(Y)]
sy, sx = Y-1, 0
count = 1
board[sy][sx] = count
di = ((-1, 0), (0, 1), (1, 0), (0, -1))
d = 0
Q = deque()
Q.append((sy, sx))
result = [0, 0]
while count < Y * X:
    y, x = Q.popleft()
    if count == Y * X:
        board[y][x] = count
        break
    if count == M:
        result = [Y - y, x + 1]
        break
    ny, nx = y + di[d][0], x + di[d][1]
    if 0 <= ny < Y and 0 <= nx < X:
        if board[ny][nx] != 0:
            d = (d + 1) % 4
            Q.append((y, x))
        else:
            count += 1
            board[ny][nx] = count
            Q.append((ny, nx))
    else:
        d = (d + 1) % 4
        Q.append((y, x))

if M > Y * X:
    print(0)
elif result == [0, 0]:
    print(Y - Q[0][0], Q[0][1] + 1)
else:
    print(*result)
