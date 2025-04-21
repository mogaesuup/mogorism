import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
  words = [input() for _ in range(5)]

  max_length = max(map(len, words))

  for i in range(max_length):
    for word in words:
      if len(word) <= i:
        continue
      print(word[i], end='')

  print() # 테스트 케이스 때문에 줄바꿈. 제출시 삭제 해도 됨


if __name__ == '__main__':
  solve()
