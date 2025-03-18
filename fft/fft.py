from math import cos, sin, pi

def fft(board, w):
    n = len(board) // 2
    if n == 0:return
    even = board[0::2]
    odd = board[1::2]
    fft(even, w * w)
    fft(odd, w * w)
    wp = complex(1, 0)
    for i in range(n):
        board[i] = even[i] + wp * odd[i]
        board[i + n] = even[i] - wp * odd[i]
        wp *= w

def multiply(A, B):
    N = max(len(A), len(B))
    n = 1
    while n <= N:
        n *= 2
    n *= 2
    A.extend([0] * (n - N))
    B.extend([0] * (n - N))
    w = complex(cos(2 * pi / n), sin(2 * pi / n))
    fft(A, w)
    fft(B, w)
    c = [A[i] * B[i] for i in range(n)]
    fft(c, 1 / w)
    return [round(c[i].real / n) for i in range(n)]
