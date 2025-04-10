import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  max = -1
  max_row_index = -0
  max_col_index = -0

  matrix = [list(map(int, input().split())) for _ in range(9)]

  for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
      if max < value:
        max = value
        max_row_index = row_index
        max_col_index = col_index

  ''.lstrip()

  print(max)
  print(max_row_index + 1, max_col_index + 1)


if __name__ == '__main__':
  solve()
