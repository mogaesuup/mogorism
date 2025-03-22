import sys
sys.stdin = open("11758.txt", "r")
input = sys.stdin.readline


x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))


def ccw(x1, y1, x2, y2, x3, y3):
    # xy2131 yx2131
    # <       |       >
    # 시계  일직선  반시계
    # -1      0       1
    temp = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if temp < 0:
        return -1
    elif temp == 0:
        return 0
    else:
        return 1


print(ccw(x1, y1, x2, y2, x3, y3))
