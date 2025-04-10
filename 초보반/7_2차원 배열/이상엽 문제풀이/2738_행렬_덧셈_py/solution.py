import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  n, m = map(int, input().split())

  matrix_a = [list(map(int, input().split())) for _ in range(n)]
  matrix_b = [list(map(int, input().split())) for _ in range(n)]

  for i in range(n):
    for j in range(m):
      matrix_a[i][j] = str(matrix_a[i][j] + matrix_b[i][j])

  print('\n'.join([' '.join(row) for row in matrix_a]))


if __name__ == '__main__':
  solve()
