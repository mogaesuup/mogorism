import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  room = int(input())
  move = 1

  max_room = 1
  while max_room < room:
    max_room += 6 * move
    move += 1

  print(move)


if __name__ == '__main__':
  solve()
