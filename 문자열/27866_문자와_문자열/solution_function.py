import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  txt = input()
  index = input()
  print(txt[int(index) - 1])


if __name__ == '__main__':
  solve()
