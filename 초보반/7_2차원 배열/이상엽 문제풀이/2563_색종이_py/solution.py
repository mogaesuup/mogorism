import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  paper_count = int(input())

  grid = [[0] * 100 for _ in range(100)]

  for _ in range(paper_count):
    x, y = map(int, input().split())
    for row in grid[x:x + 10]:
      row[y:y + 10] = [1] * 10

  print(sum(sum(row) for row in grid))


if __name__ == '__main__':
  solve()
