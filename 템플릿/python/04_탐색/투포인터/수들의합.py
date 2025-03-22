import sys
sys.stdin = open('2003.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
board = list(map(int, input().split()))
Sum = r = l = result = 0
while True:
    if Sum >= M:
        if Sum == M:
            result += 1
        Sum -= board[l]
        l -= 1
    elif Sum < M:
        if r == N:
            break
        Sum += board[r]
        r += 1
print(result)
