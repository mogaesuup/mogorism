import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  word = input()

  reversed_word = word[::-1]

  print(1 if word == reversed_word else 0)


if __name__ == '__main__':
  solve()
