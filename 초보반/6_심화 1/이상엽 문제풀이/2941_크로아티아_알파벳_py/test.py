from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ('ljes=njak', '6\n'),
  ('ddz=z=', '3\n'),
  ('nljj', '3\n'),
  ('c=c=', '2\n'),
  ('dz=ak', '3\n'),
  ('abc', '3\n'),
  ('c=c-', '2\n'),
  ('dz=dz=', '2\n'),
  ('dddz=z=', '4\n'),
  ('d-dz=', '2\n'),
  ('njnj', '2\n'),
  ('s=z=z=', '3\n'),
  ('zz=z', '3\n'),
  ('c=c=c-', '3\n'),
  ('dz=dz=z=', '3\n'),
  ('c-dz=cc=', '4\n'),
  ('d-d-d-', '3\n'),
  ('dz=dz=dz=', '3\n'),
  ('njnjnj', '3\n'),
  ('dz=dz=dz=z=', '4\n'),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
