from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ('0 1 2 2 2 7', '1 0 0 0 0 1\n'),
  ('2 1 2 1 2 1', '-1 0 0 1 0 7\n'),
  ('1 1 2 2 2 8', '0 0 0 0 0 0\n'),
  ('0 0 0 0 0 0', '1 1 2 2 2 8\n'),
  ('1 0 1 2 2 7', '0 1 1 0 0 1\n'),
  ('1 1 1 1 1 1', '0 0 1 1 1 7\n'),
  ('0 0 2 2 2 8', '1 1 0 0 0 0\n'),
  ('1 1 0 0 0 0', '0 0 2 2 2 8\n'),
  ('0 0 0 2 2 8', '1 1 2 0 0 0\n'),
  ('0 1 0 2 0 8', '1 0 2 0 2 0\n'),
  ('1 0 2 2 2 8', '0 1 0 0 0 0\n'),
  ('0 1 1 1 2 8', '1 0 1 1 0 0\n'),
  ('1 1 2 0 2 8', '0 0 0 2 0 0\n'),
  ('1 1 2 2 0 0', '0 0 0 0 2 8\n'),
  ('2 2 2 2 2 2', '-1 -1 0 0 0 6\n'),
  ('0 2 2 2 2 8', '1 -1 0 0 0 0\n'),
  ('0 0 2 1 2 8', '1 1 0 1 0 0\n'),
  ('1 1 0 0 2 7', '0 0 2 2 0 1\n'),
  ('0 1 1 2 1 8', '1 0 1 0 1 0\n'),
  ('1 0 1 2 1 7', '0 1 1 0 1 1\n'),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
