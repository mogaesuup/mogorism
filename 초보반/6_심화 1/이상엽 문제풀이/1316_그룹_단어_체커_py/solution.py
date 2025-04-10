import sys

input = lambda: sys.stdin.readline().rstrip()


def is_group_word(word):
  for i in range(1, len(word)):
    is_not_same_char = word[i] != word[i - 1]
    is_contain_prev = word[i] in word[:i]
    if is_not_same_char and is_contain_prev:
      return False
  return True


def solve():
  n = int(input())

  group_word_count = 0

  for i in range(n):
    word = input()

    if is_group_word(word):
      group_word_count += 1

  print(group_word_count)


if __name__ == '__main__':
  solve()
