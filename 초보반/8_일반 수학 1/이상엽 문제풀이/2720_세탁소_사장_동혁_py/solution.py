import sys

input = lambda: sys.stdin.readline().rstrip()

coin_value = [25, 10, 5, 1]


def solve():
  test_case = int(input())

  for _ in range(test_case):
    coins = [0] * 4
    change = int(input())

    for i, val in enumerate(coin_value):
      coins[i] = change // val
      change = change % val

    print(*coins)


if __name__ == '__main__':
  solve()
