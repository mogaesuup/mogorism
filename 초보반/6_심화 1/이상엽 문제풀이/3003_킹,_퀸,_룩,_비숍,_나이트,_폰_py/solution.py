import sys

input = lambda: sys.stdin.readline().rstrip()

correct_pieces_count = [1, 1, 2, 2, 2, 8]


def solve():
  pieces_count = list(map(int, input().split()))
  diff_count = []

  for i in range(6):
    diff_count.append(str(correct_pieces_count[i] - pieces_count[i]))

  print(' '.join(diff_count))


if __name__ == '__main__':
  solve()
