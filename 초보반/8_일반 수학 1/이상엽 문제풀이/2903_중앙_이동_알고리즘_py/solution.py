import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  n = int(input())
  print((2 ** n + 1) ** 2)


if __name__ == '__main__':
  solve()
