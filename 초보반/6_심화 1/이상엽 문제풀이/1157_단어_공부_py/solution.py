import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  word = input().upper()
  alphabet_list = set(word)

  max_count = -1
  result = ''

  for alphabet in alphabet_list:
    alphabet_count = word.count(alphabet)
    if alphabet_count == max_count:
      result = '?'
    if alphabet_count > max_count:
      max_count = alphabet_count
      result = alphabet

  print(result)


if __name__ == '__main__':
  solve()
