import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  n = int(input())

  for top in range(1, n + 1):
    top_space = ' ' * (n - top)
    top_star = '*' * (top * 2 - 1)
    print(top_space + top_star)

  for bottom in range(1, n):
    bottom_space = ' ' * bottom
    bottom_star = '*' * ((n - bottom) * 2 - 1)
    print(bottom_space + bottom_star)


if __name__ == '__main__':
  solve()
