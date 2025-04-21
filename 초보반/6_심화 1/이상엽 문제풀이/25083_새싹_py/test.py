from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  ('', """         ,r'"7
r`-_   ,'  ,/
 \\. ". L_r'
   `~\\/
      |
      |
""")
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
