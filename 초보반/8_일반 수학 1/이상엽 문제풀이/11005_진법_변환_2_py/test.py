from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: 1을 2진법으로 변환 → 1
  (
    "1 2\n",
    "1\n"
  ),
  # 테스트 케이스 2: 10을 2진법으로 변환 → 1010
  (
    "10 2\n",
    "1010\n"
  ),
  # 테스트 케이스 3: 255를 16진법으로 변환 → FF
  (
    "255 16\n",
    "FF\n"
  ),
  # 테스트 케이스 4: 1000을 36진법으로 변환 → RS
  (
    "1000 36\n",
    "RS\n"
  ),
  # 테스트 케이스 5: 36을 36진법으로 변환 → 10
  (
    "36 36\n",
    "10\n"
  ),
  # 테스트 케이스 6: 123456789를 8진법으로 변환 → 726746425
  (
    "123456789 8\n",
    "726746425\n"
  ),
  # 테스트 케이스 7: 1000000000을 16진법으로 변환 → 3B9ACA00
  (
    "1000000000 16\n",
    "3B9ACA00\n"
  ),
  # 테스트 케이스 8: 35를 35진법으로 변환 → 10
  (
    "35 35\n",
    "10\n"
  ),
  # 테스트 케이스 9: 100을 2진법으로 변환 → 1100100
  (
    "100 2\n",
    "1100100\n"
  ),
  # 테스트 케이스 10: 987654321을 36진법으로 변환 → GC0UY9
  (
    "987654321 36\n",
    "GC0UY9\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
