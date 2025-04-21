import sys

input = lambda: sys.stdin.readline().rstrip()

croatia_alphabets = [
  'c=',
  'c-',
  'dz=',
  'd-',
  'lj',
  'nj',
  's=',
  'z=',
]


def solve():
  word = input()
  for croatia_alphabet in croatia_alphabets:
    word = word.replace(croatia_alphabet, ' ')

  print(len(word))


if __name__ == '__main__':
  solve()
