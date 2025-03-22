import sys
sys.stdin = open('17298.txt', 'r')

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = [0]*n
s = [0]
for i in range(1, n):
    if not s:
        s.append(i)
    while s and a[s[-1]] < a[i]:
        ans[s.pop()] = a[i]
    s.append(i)
while s:
    ans[s.pop()] = -1
print(' '.join(map(str, ans)))
