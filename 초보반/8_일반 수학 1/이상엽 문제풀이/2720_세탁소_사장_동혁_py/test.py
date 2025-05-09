from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: 단일 테스트 케이스 - 1센트 → 0 0 0 1
  (
    "1\n"
    "1\n",
    "0 0 0 1\n"
  ),
  # 테스트 케이스 2: 단일 테스트 케이스 - 6센트 → 0 0 1 1
  (
    "1\n"
    "6\n",
    "0 0 1 1\n"
  ),
  # 테스트 케이스 3: 단일 테스트 케이스 - 49센트 → 1 2 0 4
  (
    "1\n"
    "49\n",
    "1 2 0 4\n"
  ),
  # 테스트 케이스 4: 2개의 테스트 케이스 - 25센트와 26센트
  # 25센트 → 1 0 0 0, 26센트 → 1 0 0 1
  (
    "2\n"
    "25\n"
    "26\n",
    "1 0 0 0\n"
    "1 0 0 1\n"
  ),
  # 테스트 케이스 5: 3개의 테스트 케이스 - 100, 99, 50센트
  # 100센트 → 4 0 0 0, 99센트 → 3 2 0 4, 50센트 → 2 0 0 0
  (
    "3\n"
    "100\n"
    "99\n"
    "50\n",
    "4 0 0 0\n"
    "3 2 0 4\n"
    "2 0 0 0\n"
  ),
  # 테스트 케이스 6: 4개의 테스트 케이스 - 37, 45, 30, 89센트
  # 37 → 1 1 0 2, 45 → 1 2 0 0, 30 → 1 0 1 0, 89 → 3 1 0 4
  (
    "4\n"
    "37\n"
    "45\n"
    "30\n"
    "89\n",
    "1 1 0 2\n"
    "1 2 0 0\n"
    "1 0 1 0\n"
    "3 1 0 4\n"
  ),
  # 테스트 케이스 7: 5개의 테스트 케이스 - 5, 10, 15, 20, 100센트
  # 5 → 0 0 1 0, 10 → 0 1 0 0, 15 → 0 1 1 0, 20 → 0 2 0 0, 100 → 4 0 0 0
  (
    "5\n"
    "5\n"
    "10\n"
    "15\n"
    "20\n"
    "100\n",
    "0 0 1 0\n"
    "0 1 0 0\n"
    "0 1 1 0\n"
    "0 2 0 0\n"
    "4 0 0 0\n"
  ),
  # 테스트 케이스 8: 2개의 테스트 케이스 - 큰 값: 1000, 999센트
  # 1000 → 40 0 0 0, 999 → 39 2 0 4
  (
    "2\n"
    "1000\n"
    "999\n",
    "40 0 0 0\n"
    "39 2 0 4\n"
  ),
  # 테스트 케이스 9: 3개의 테스트 케이스 - 경계값: 24, 25, 26센트
  # 24 → 0 2 0 4, 25 → 1 0 0 0, 26 → 1 0 0 1
  (
    "3\n"
    "24\n"
    "25\n"
    "26\n",
    "0 2 0 4\n"
    "1 0 0 0\n"
    "1 0 0 1\n"
  ),
  # 테스트 케이스 10: 4개의 테스트 케이스 - 임의의 값: 73, 84, 95, 87센트
  # 73 → 2 2 0 3, 84 → 3 0 1 4, 95 → 3 2 0 0, 87 → 3 1 0 2
  (
    "4\n"
    "73\n"
    "84\n"
    "95\n"
    "87\n",
    "2 2 0 3\n"
    "3 0 1 4\n"
    "3 2 0 0\n"
    "3 1 0 2\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
