import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  paper_count = int(input())

  grid = [[0] * 30 for _ in range(30)]

  for _ in range(paper_count):
    x, y = map(int, input().split())
    for row in grid[x:x + 10]:
      row[y:y + 10] = [1] * 10
    print('\n'.join(''.join(list(map(lambda x: '■' if x == 1 else '□', row))) for row in grid))
    print()
    print()

  print(sum(sum(row) for row in grid))


if __name__ == '__main__':
  solve()

#3
#3 7
#15 7
#5 2
