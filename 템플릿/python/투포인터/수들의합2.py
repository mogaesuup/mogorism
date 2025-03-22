import sys
sys.stdin = open('2003.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
board = list(map(int, input().split()))
Sum = right = left = result = 0
while True:
    if Sum >= M:
        if Sum == M:
            result += 1
        Sum -= board[left]
        left += 1
    elif Sum < M:
        if right == N:
            break
        Sum += board[right]
        right += 1
print(result)
