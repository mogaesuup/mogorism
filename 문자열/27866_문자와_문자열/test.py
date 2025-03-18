from solution_function import solve
from util.test_runner import run_fun_solution, run_solution

test_cases = [
  ("Baekjoon\n1\n", "B\n"),
  ("Baekjoon\n4\n", "k\n"),
  ("Hello\n2\n", "e\n"),
  ("Python\n1\n", "P\n"),
  ("algorithm\n5\n", "r\n"),
  ("contest\n7\n", "t\n"),
  ("developer\n4\n", "e\n"),
  ("acmicpc\n3\n", "m\n"),
  ("example\n2\n", "x\n"),
  ("random\n6\n", "m\n"),
  ("testing\n4\n", "t\n"),
  ("pytest\n3\n", "t\n"),
  ("solution\n8\n", "n\n"),
  ("keyboard\n5\n", "o\n"),
  ("monitor\n2\n", "o\n"),
  ("laptop\n1\n", "l\n"),
  ("desktop\n7\n", "p\n"),
  ("internet\n4\n", "e\n"),
  ("programming\n6\n", "a\n"),
  ("challenge\n9\n", "e\n")
]


def test_fun():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"


def test():
  for input_data, expected_output in test_cases:
    output = run_solution(input_data, __file__, "solution.py")
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
