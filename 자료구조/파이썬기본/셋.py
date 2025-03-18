a = {1, 2}
# 삽입
a.add(3)
# {1, 2, 3}
print(a)
# 업데이트
b = {7, 8}
a.update([4, 5, 6])
a.update(b)
# {1, 2, 3, 4, 5, 6, 7, 8}
print(a)
# 삭제
a.remove(1)
# {2, 3, 4, 5, 6, 7, 8}
print(a)

# 합집합
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = a | b
d = a.union(b)
# {1, 2, 3, 4, 5, 6, 7}
print(c)
print(d)

# 교집합
c = a & b
d = a.intersection(b)
# {3, 4, 5}
print(c)
print(d)

# 차집합
c = a - b
d = b - a
e = a.difference(b)
# {1, 2}
print(c)
# {6, 7}
print(d)
# {1, 2}
print(e)

# 대칭 차집합
c = a ^ b
d = a.symmetric_difference(b)
# {1, 2, 6, 7}
print(c)
# {1, 2, 6, 7}
print(d)


# 부분집합 확인 issubset
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
# False
print(a.issubset(b))
# True
print(b.issubset(a))
# 부분집합 확인 반대 issuperset
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
# False
print(a.issuperset(b))
# True
print(b.issuperset(a))
# 교집합 확인(없으면 True)
a = {1, 2, 3}
b = {4, 5, 6}
# True
print(a.isdisjoint(b))
c = {1, 2, 3}
d = {3, 4, 5}
# False
print(c.isdisjoint(d))
