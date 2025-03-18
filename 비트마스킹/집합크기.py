# 집합 크기
# b = 1000011
b = 67


def bitCount(x):
    if x == 0:
        return 0
    return x % 2 + bitCount(x // 2)


print(bitCount(b))

count = 0
while b > 0:
    count += b % 2
    b //= 2
print(count)
