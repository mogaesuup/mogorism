import sys
sys.stdin = open("템플릿/python/09_기하/CCW/17386.txt", "r")
input = sys.stdin.readline

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(A, B, C):
    return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)

def is_intersect(A, B, C, D):
    return ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())    
A = P(x1, y1)
B = P(x2, y2)
C = P(x3, y3)
D = P(x4, y4)

if is_intersect(A, B, C, D):
    print(1)
else:
    print(0)
