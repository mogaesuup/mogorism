from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: 이진수 1을 2진법으로 표현 → 1
  (
    "1 2\n",
    "1\n"
  ),
  # 테스트 케이스 2: 십진수 10을 10진법으로 표현 → 10
  (
    "10 10\n",
    "10\n"
  ),
  # 테스트 케이스 3: 16진수 A를 16진법으로 표현 → 10
  (
    "A 16\n",
    "10\n"
  ),
  # 테스트 케이스 4: 이진수 1010을 2진법으로 표현 → 10
  (
    "1010 2\n",
    "10\n"
  ),
  # 테스트 케이스 5: 36진수 ZZZZZ → 60466175
  (
    "ZZZZZ 36\n",
    "60466175\n"
  ),
  # 테스트 케이스 6: 30진수 HELLO (H=17, E=14, L=21, O=24) → 14167554
  (
    "HELLO 30\n",
    "14167554\n"
  ),
  # 테스트 케이스 7: 앞에 불필요한 0가 붙은 0001 (10진법) → 1
  (
    "0001 10\n",
    "1\n"
  ),
  # 테스트 케이스 8: 36진수 ZZZZZZZZZZ (10자리 모두 Z) → 36^10 - 1 = 3656158440062975
  (
    "ZZZZZZZZZZ 36\n",
    "3656158440062975\n"
  ),
  # 테스트 케이스 9: 6진수 12345 → 1×6⁴ + 2×6³ + 3×6² + 4×6¹ + 5 = 1865
  (
    "12345 6\n",
    "1865\n"
  ),
  # 테스트 케이스 10: 16진수 ABCDEF → 11259375
  (
    "ABCDEF 16\n",
    "11259375\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
