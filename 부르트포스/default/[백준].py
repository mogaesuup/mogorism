import sys
sys.stdin = open('5543.txt', 'r')

SB = int(input())
GB = int(input())
HB = int(input())
C = int(input())
S = int(input())
MB = min(SB, GB, HB)
MC = min(C, S)
print(MB + MC - 50)
