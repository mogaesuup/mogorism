import sys
sys.stdin = open("20057.txt", "r")
input = sys.stdin.readline
di = ((0, -1), (1, 0), (0, 1), (-1, 0))
N = int(input())
board = [[0] * N for _ in range(N)]
y = x = N // 2
count = 1
d = 0
while True:
    if 0 <= x < N and 0 <= y < N:
        board[y][x] = count
        count += 1
        y, x = y + di[d][0], x + di[d][1]
        if board[y + di[(d + 1) % 4][0]][x + di[(d + 1) % 4][1]] == 0:
            d = (d + 1) % 4
    else:
        break
for b in board:
    print(*b)
