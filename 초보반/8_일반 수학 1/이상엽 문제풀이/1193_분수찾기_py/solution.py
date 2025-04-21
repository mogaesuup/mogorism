import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  x = int(input())

  remain = x
  layer = 1

  while remain > layer:
    remain -= layer
    layer += 1

  if layer % 2 == 0:
    print('{}/{}'.format(remain, layer + 1 - remain))
  else:
    print('{}/{}'.format(layer + 1 - remain, remain))


if __name__ == '__main__':
  solve()
