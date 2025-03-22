import sys
sys.stdin = open('./test/2188.txt', 'r')
input = sys.stdin.readline
def dfs(n):
    # 이미 방문했으면 
    if N[n]: return False
    N[n] = True
    for m in g[n]:
        # M이 열려있으면 바로 true 혹은 N을 이미 방문했지만 바꾸는게 가능할 경우 True 반환
        if not M[m] or dfs(M[m]):
            # 다시 닫아주고 M에는 서로의 매칭된 곳 기입, N은 방문표시
            M[m] = n
            return True
    # 실패
    return False
n, m = map(int, input().split())
g = {}
for i in range(1, n + 1):
    g[i] = list(map(int, input().split()))[1:]
M = [False for _ in range(m + 1)]
result = 0
for i in range(1, n + 1):
    N = [False for _ in range(n + 1)]
    if dfs(i):
        result += 1
print(result)
