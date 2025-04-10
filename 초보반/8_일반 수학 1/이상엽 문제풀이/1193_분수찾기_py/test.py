from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: X = 1 → 첫 번째 분수는 "1/1"
  (
    "1\n",
    "1/1\n"
  ),
  # 테스트 케이스 2: X = 2 → 두 번째 분수는 "1/2"
  (
    "2\n",
    "1/2\n"
  ),
  # 테스트 케이스 3: X = 3 → 세 번째 분수는 "2/1"
  (
    "3\n",
    "2/1\n"
  ),
  # 테스트 케이스 4: X = 4 → 네 번째 분수는 "3/1"
  (
    "4\n",
    "3/1\n"
  ),
  # 테스트 케이스 5: X = 5 → 다섯 번째 분수는 "2/2"
  (
    "5\n",
    "2/2\n"
  ),
  # 테스트 케이스 6: X = 6 → 여섯 번째 분수는 "1/3"
  (
    "6\n",
    "1/3\n"
  ),
  # 테스트 케이스 7: X = 7 → 일곱 번째 분수는 "1/4"
  (
    "7\n",
    "1/4\n"
  ),
  # 테스트 케이스 8: X = 8 → 여덟 번째 분수는 "2/3"
  (
    "8\n",
    "2/3\n"
  ),
  # 테스트 케이스 9: X = 14
  # 1+2+3+4 = 10이므로, 5번째 대각선에 해당하며, r = 14 - 10 = 4
  # n = 5 (홀수)이므로 분수는 (n - r + 1) / r = (5 - 4 + 1) / 4 = 2/4
  (
    "14\n",
    "2/4\n"
  ),
  # 테스트 케이스 10: X = 10000000 (큰 입력)
  # n = ceil((sqrt(8*10000000+1)-1)/2) = 4472
  # 이전까지의 개수 T = (4471*4472)/2 = 9,997,156
  # r = 10000000 - 9,997,156 = 2844
  # n = 4472 (짝수)이므로 분수는 r/(n - r + 1) = 2844/(4472 - 2844 + 1) = 2844/1629
  (
    "10000000\n",
    "2844/1629\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
