import sys
sys.stdin = open("17276.txt", "r")
input = sys.stdin.readline
for _ in range(int(input())):
    N, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    if d < 0:
        d += 360
    N_ = N // 2
    di = [[] for _ in range(4)]
    values = [[] for _ in range(4)]
    for i in range(N):
        di[0].append((i, i))
        values[0].append(board[i][i])
    for i in range(N):
        di[1].append((i, N_))
        values[1].append(board[i][N_])
    for i in range(N-1, -1, -1):
        di[2].append((~i, i))
        values[2].append(board[~i][i])
    for i in range(N-1, -1, -1):
        di[3].append((N_, i))
        values[3].append(board[N_][i])
    di += list(map(lambda di: di[::-1], di))
    values += list(map(lambda di: di[::-1], values))
    turn = d // 45
    _values = values[8 - turn:] + values[:8 - turn]
    for j in range(8):
        for i in range(N):
            ny, nx = di[j][i]
            val = _values[j][i]
            board[ny][nx] = val
    list(map(lambda a: print(*a), board))
