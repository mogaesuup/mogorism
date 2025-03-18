from collections import deque

Q = deque('love')
print(Q)
# deque(['l', 'o', 'v', 'e'])


# 1. 스택 구현: append(), pop()
Q.append('m')
# deque(['l', 'o', 'v', 'e', 'm'])
print(Q)
# deque(['l', 'o', 'v', 'e'])
print(Q.pop())
print(Q)

# 2. 큐 구현 : appendleft(), pop(), append(), popleft()
Q.appendleft('I')
# 왼쪽에서 'I'입력
# deque(['I', 'l', 'o', 'v', 'e'])
print(Q)
# 오른쪽에서 'e'출력
print(deque(['I', 'l', 'o', 'v']))
print(Q.pop())

# 3. extend(), extendleft()

# 오른쪽으로 'y','o','u' 확장
Q.extend('you')
# deque(['l', 'o', 'v', 'e', 'y', 'o', 'u'])
print(Q)

# 왼쪽으로 'I' 확장
Q.extendleft('I')
# deque(['I', 'l', 'o', 'v', 'e', 'y', 'o', 'u'])
print(Q)

# 4. 리스트처럼 사용: insert(), remove()
Q[2] = 'n'
# 인덱스를 이용한 항목 수정 'v' => 'n'
# deque(['l', 'o', 'n', 'e'])
print(Q)

Q = deque('love')
# 첫번째 항목에 'K'를 추가
Q.insert(0, 'K')
# deque(['K', 'l', 'o', 'v', 'e'])
print(Q)

# 100번째 항목(없으니까 가장 큰 쪽에)에 'K' 추가
Q.insert(100, 'K')
# deque(['K', 'l', 'o', 'v', 'e', 'K'])
print(Q)

# 'K'항목 삭제
Q.remove('K')
# 같은 항목이 있을때 지우면 왼쪽부터 삭제
# deque(['l', 'o', 'v', 'e', 'K'])
print(Q)

# 오른쪽에 있는 'K'삭제
Q.remove('K')
# deque(['l', 'o', 'v', 'e'])
print(Q)

# 5. 좌우 반전 reverse
# deque(['l', 'o', 'v', 'e'])
Q.reverse()
# deque(['e', 'v', 'o', 'l'])
print(Q)

# 6. 회전 rotate
Q = deque([1, 2, 3, 4, 5])
Q.rotate(1)
# deque([5, 1, 2, 3, 4])
print(Q)
Q.rotate(-1)
print(Q)
