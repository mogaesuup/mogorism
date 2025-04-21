from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: N = 0 → (2^0 + 1)² = (1 + 1)² = 4
  (
    "0\n",
    "4\n"
  ),
  # 테스트 케이스 2: N = 1 → (2^1 + 1)² = (2 + 1)² = 9
  (
    "1\n",
    "9\n"
  ),
  # 테스트 케이스 3: N = 2 → (2^2 + 1)² = (4 + 1)² = 25
  (
    "2\n",
    "25\n"
  ),
  # 테스트 케이스 4: N = 3 → (2^3 + 1)² = (8 + 1)² = 81
  (
    "3\n",
    "81\n"
  ),
  # 테스트 케이스 5: N = 4 → (2^4 + 1)² = (16 + 1)² = 289
  (
    "4\n",
    "289\n"
  ),
  # 테스트 케이스 6: N = 5 → (2^5 + 1)² = (32 + 1)² = 1089
  (
    "5\n",
    "1089\n"
  ),
  # 테스트 케이스 7: N = 6 → (2^6 + 1)² = (64 + 1)² = 4225
  (
    "6\n",
    "4225\n"
  ),
  # 테스트 케이스 8: N = 7 → (2^7 + 1)² = (128 + 1)² = 16641
  (
    "7\n",
    "16641\n"
  ),
  # 테스트 케이스 9: N = 8 → (2^8 + 1)² = (256 + 1)² = 66049
  (
    "8\n",
    "66049\n"
  ),
  # 테스트 케이스 10: N = 10 → (2^10 + 1)² = (1024 + 1)² = 1050625
  (
    "10\n",
    "1050625\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
