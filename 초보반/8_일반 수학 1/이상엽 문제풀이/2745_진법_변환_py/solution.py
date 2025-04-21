import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  number, base = input().split()
  print(int(number, int(base)))


if __name__ == '__main__':
  solve()
