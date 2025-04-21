import math
import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  climb, slide, target = map(int, input().split())
  print(math.ceil((target - slide) / (climb - slide)))


if __name__ == '__main__':
  solve()
