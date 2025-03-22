arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = 3
# 90도 한줄
rotated = list(zip(*reversed(arr)))

# 90도
one = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        one[x][N - 1 - y] = arr[y][x]
# 180도
two = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        two[N - 1 - y][N - 1 - x] = arr[y][x]
# 270도
three = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        three[N - 1 - x][y] = arr[y][x]
# 전치행렬
four = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        four[x][y] = arr[y][x]

print(one)
print(two)
print(three)
print(four)
