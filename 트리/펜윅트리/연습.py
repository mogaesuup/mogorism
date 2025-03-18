# 2의 보수 ex) 5 = 0101에서 1010으로 바꾼 후 +1 = 1011
for i in range(10):
    print(i, bin(i), bin(-i), bin(i & -i))
