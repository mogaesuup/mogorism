import sys
sys.stdin = open("2003.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
left = right = 0
Sum = A[0]
result = 0
while left <= right and right < N:
    if Sum < M:
        right += 1
        if right < N:
            Sum += A[right]
    elif Sum == M:
        result += 1
        right += 1
        if right < N:
            Sum += A[right]
    elif Sum > M:
        Sum -= A[left]
        left += 1
        if left > right and left < N:
            right = left
            Sum = A[left]
print(result)
