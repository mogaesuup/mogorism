from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: N = 1 → 1번 방은 시작 방이므로 1
  (
    "1\n",
    "1\n"
  ),
  # 테스트 케이스 2: N = 2 → 2번 방은 2번째 층에 있으므로 2
  (
    "2\n",
    "2\n"
  ),
  # 테스트 케이스 3: N = 7 → 7번까지는 2번째 층, 따라서 2
  (
    "7\n",
    "2\n"
  ),
  # 테스트 케이스 4: N = 8 → 8번부터 19번까지는 3번째 층, 따라서 3
  (
    "8\n",
    "3\n"
  ),
  # 테스트 케이스 5: N = 19 → 여전히 3번째 층에 속하므로 3
  (
    "19\n",
    "3\n"
  ),
  # 테스트 케이스 6: N = 20 → 20번부터 37번까지는 4번째 층, 따라서 4
  (
    "20\n",
    "4\n"
  ),
  # 테스트 케이스 7: N = 37 → 4번째 층의 마지막 번호이므로 4
  (
    "37\n",
    "4\n"
  ),
  # 테스트 케이스 8: N = 38 → 38번부터 61번까지는 5번째 층, 따라서 5
  (
    "38\n",
    "5\n"
  ),
  # 테스트 케이스 9: N = 58 → 38 ≤ 58 ≤ 61, 5번째 층에 속하므로 5
  (
    "58\n",
    "5\n"
  ),
  # 테스트 케이스 10: 큰 수 예시
  # N = 1,000,000인 경우, 1 + 3×n×(n-1) ≥ 1,000,000를 만족하는 최소 n는 578
  (
    "1000000\n",
    "578\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
