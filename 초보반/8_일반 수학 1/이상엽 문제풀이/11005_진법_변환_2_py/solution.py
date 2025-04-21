import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  number, base = map(int, input().split())
  result_reverse = ''

  while number > 0:
    number, mod = divmod(number, base)
    if mod >= 10:
      mod += 55
      result_reverse += chr(mod)
    else:
      result_reverse += str(mod)

  print(result_reverse[::-1])


if __name__ == '__main__':
  solve()
