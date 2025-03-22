import sys

input = lambda: sys.stdin.readline().rstrip()

txt = input()
index = input()
print(txt[int(index) - 1])
