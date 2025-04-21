from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ('Mississipi', '?\n'),
  ('zZa', 'Z\n'),
  ('z', 'Z\n'),
  ('baaa', 'A\n'),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
