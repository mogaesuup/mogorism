import sys
sys.stdin = open("17276.txt", "r")
input = sys.stdin.readline
for _ in range(int(input())):
    N, d = map(int, input().split())
    d //= 45
    d %= 8
    board = [list(map(int, input().split())) for i in range(N)]
    N_ = N // 2
    di = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    for i in range(1, N // 2+1):
        points = [(N_ + i * di[j][0], N_ + i * di[j][1]) for j in range(8)]
        nums = [board[i][j] for i, j in points]
        points = points[d:] + points[:d]
        for k, (i, j) in enumerate(points):
            board[i][j] = nums[k]
    list(map(lambda a: print(*a), board))
