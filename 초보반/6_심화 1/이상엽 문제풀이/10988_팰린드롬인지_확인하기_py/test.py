from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ('a', '1\n'),
  ('aa', '1\n'),
  ('ab', '0\n'),
  ('aba', '1\n'),
  ('abc', '0\n'),
  ('abba', '1\n'),
  ('abca', '0\n'),
  ('racecar', '1\n'),
  ('noon', '1\n'),
  ('abcba', '1\n'),
  ('abcbA', '0\n'),
  ('ababa', '1\n'),
  ('abcd', '0\n'),
  ('qwerty', '0\n'),
  ('level', '1\n'),
  ('radar', '1\n'),
  ('world', '0\n'),
  ('civic', '1\n'),
  ('deified', '1\n'),
  ('palindrome', '0\n'),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
