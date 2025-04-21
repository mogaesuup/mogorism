import math
from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  (
    "Course1 3.0 A+\n"
    "Course2 3.0 A0\n"
    "Course3 3.0 B+\n"
    "Course4 3.0 B0\n"
    "Course5 3.0 C+\n"
    "Course6 3.0 C0\n"
    "Course7 3.0 D+\n"
    "Course8 3.0 D0\n"
    "Course9 3.0 F\n"
    "Course10 3.0 A+\n"
    "Course11 3.0 A0\n"
    "Course12 3.0 B+\n"
    "Course13 3.0 B0\n"
    "Course14 3.0 C+\n"
    "Course15 3.0 C0\n"
    "Course16 3.0 D+\n"
    "Course17 3.0 D0\n"
    "Course18 3.0 F\n"
    "Course19 3.0 A+\n"
    "Course20 3.0 A0\n",
    "2.625\n"
  ),
  (
    "Course1 3.0 A+\n"
    "Course2 3.0 P\n"
    "Course3 3.0 A+\n"
    "Course4 3.0 P\n"
    "Course5 3.0 A+\n"
    "Course6 3.0 P\n"
    "Course7 3.0 A+\n"
    "Course8 3.0 P\n"
    "Course9 3.0 A+\n"
    "Course10 3.0 P\n"
    "Course11 3.0 A+\n"
    "Course12 3.0 P\n"
    "Course13 3.0 A+\n"
    "Course14 3.0 P\n"
    "Course15 3.0 A+\n"
    "Course16 3.0 P\n"
    "Course17 3.0 A+\n"
    "Course18 3.0 P\n"
    "Course19 3.0 A+\n"
    "Course20 3.0 P\n",
    "4.5\n"
  ),
  (
    "Course1 1.0 A0\n"
    "Course2 2.0 B0\n"
    "Course3 3.0 C0\n"
    "Course4 1.5 D0\n"
    "Course5 2.5 F\n"
    "Course6 1.0 A0\n"
    "Course7 2.0 B0\n"
    "Course8 3.0 C0\n"
    "Course9 1.5 D0\n"
    "Course10 2.5 F\n"
    "Course11 1.0 A0\n"
    "Course12 2.0 B0\n"
    "Course13 3.0 C0\n"
    "Course14 1.5 D0\n"
    "Course15 2.5 F\n"
    "Course16 1.0 A0\n"
    "Course17 2.0 B0\n"
    "Course18 3.0 C0\n"
    "Course19 1.5 D0\n"
    "Course20 2.5 F\n",
    "1.75\n"
  ),
  (
    "Course1 3.0 P\n"
    "Course2 3.0 P\n"
    "Course3 3.0 P\n"
    "Course4 3.0 P\n"
    "Course5 3.0 P\n"
    "Course6 3.0 P\n"
    "Course7 3.0 P\n"
    "Course8 3.0 P\n"
    "Course9 3.0 P\n"
    "Course10 3.0 P\n"
    "Course11 3.0 P\n"
    "Course12 3.0 P\n"
    "Course13 3.0 P\n"
    "Course14 3.0 P\n"
    "Course15 3.0 P\n"
    "Course16 3.0 P\n"
    "Course17 3.0 P\n"
    "Course18 3.0 P\n"
    "Course19 3.0 P\n"
    "Course20 3.0 F\n",
    "0.0\n"
  ),
  (
    "Math 3.0 A+\n"
    "Physics 4.0 A0\n"
    "Chemistry 2.0 B+\n"
    "Biology 1.0 B0\n"
    "English 3.0 C+\n"
    "History 2.0 C0\n"
    "Geography 1.0 D+\n"
    "Art 3.0 D0\n"
    "Music 2.0 F\n"
    "PE 1.0 P\n"
    "Computer 3.0 A+\n"
    "Economics 3.0 A0\n"
    "Law 2.0 B+\n"
    "Philosophy 1.0 B0\n"
    "Sociology 2.0 C+\n"
    "Psychology 3.0 C0\n"
    "Literature 2.0 D+\n"
    "Drama 1.0 D0\n"
    "Foreign 3.0 F\n"
    "Elective 2.0 P\n",
    "2.5854\n"
  ),
  (
    "Course1 3.0 F\n"
    "Course2 3.0 F\n"
    "Course3 3.0 F\n"
    "Course4 3.0 F\n"
    "Course5 3.0 F\n"
    "Course6 3.0 F\n"
    "Course7 3.0 F\n"
    "Course8 3.0 F\n"
    "Course9 3.0 F\n"
    "Course10 3.0 F\n"
    "Course11 3.0 F\n"
    "Course12 3.0 F\n"
    "Course13 3.0 F\n"
    "Course14 3.0 F\n"
    "Course15 3.0 F\n"
    "Course16 3.0 F\n"
    "Course17 3.0 F\n"
    "Course18 3.0 F\n"
    "Course19 3.0 P\n"
    "Course20 3.0 P\n",
    "0.0\n"
  ),
  (
    "Course1 1.0 A+\n"
    "Course2 2.0 A0\n"
    "Course3 3.0 B+\n"
    "Course4 4.0 B0\n"
    "Course5 1.0 C+\n"
    "Course6 2.0 C0\n"
    "Course7 3.0 D+\n"
    "Course8 4.0 D0\n"
    "Course9 1.0 F\n"
    "Course10 2.0 P\n"
    "Course11 3.0 A+\n"
    "Course12 4.0 A0\n"
    "Course13 1.0 B+\n"
    "Course14 2.0 B0\n"
    "Course15 3.0 C+\n"
    "Course16 4.0 C0\n"
    "Course17 1.0 D+\n"
    "Course18 2.0 D0\n"
    "Course19 3.0 F\n"
    "Course20 4.0 P\n",
    "2.4545\n"
  ),
  (
    "Course1 4.0 A+\n"
    "Course2 4.0 A+\n"
    "Course3 4.0 A+\n"
    "Course4 4.0 A+\n"
    "Course5 4.0 A+\n"
    "Course6 4.0 A+\n"
    "Course7 4.0 A+\n"
    "Course8 4.0 A+\n"
    "Course9 4.0 A+\n"
    "Course10 4.0 A+\n"
    "Course11 4.0 A+\n"
    "Course12 4.0 A+\n"
    "Course13 4.0 A+\n"
    "Course14 4.0 A+\n"
    "Course15 4.0 A+\n"
    "Course16 4.0 A+\n"
    "Course17 4.0 A+\n"
    "Course18 4.0 A+\n"
    "Course19 4.0 A+\n"
    "Course20 4.0 A+\n",
    "4.5\n"
  ),
  (
    "Course1 3.0 F\n"
    "Course2 3.0 F\n"
    "Course3 3.0 F\n"
    "Course4 3.0 F\n"
    "Course5 3.0 F\n"
    "Course6 3.0 F\n"
    "Course7 3.0 F\n"
    "Course8 3.0 F\n"
    "Course9 3.0 F\n"
    "Course10 3.0 F\n"
    "Course11 3.0 F\n"
    "Course12 3.0 F\n"
    "Course13 3.0 F\n"
    "Course14 3.0 F\n"
    "Course15 3.0 F\n"
    "Course16 3.0 F\n"
    "Course17 3.0 F\n"
    "Course18 3.0 F\n"
    "Course19 3.0 F\n"
    "Course20 3.0 F\n",
    "0.0\n"
  ),
  (
    "Eng1 2.0 A+\n"
    "Eng2 3.0 P\n"
    "Math1 4.0 B0\n"
    "Math2 1.0 C+\n"
    "Hist1 3.0 D0\n"
    "Hist2 2.0 P\n"
    "Sci1 3.0 A0\n"
    "Sci2 2.0 B+\n"
    "Bio1 1.0 F\n"
    "Bio2 3.0 D+\n"
    "Art1 2.0 A+\n"
    "Art2 3.0 A+\n"
    "Lang1 4.0 B0\n"
    "Lang2 1.0 C0\n"
    "Comp1 3.0 A0\n"
    "Comp2 2.0 P\n"
    "PE1 3.0 D0\n"
    "PE2 1.0 F\n"
    "Elective1 3.0 C+\n"
    "Elective2 2.0 P\n",
    "2.7949\n"
  )
]

def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"

def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    try:
      expected_val = float(expected_output.strip())
      output_val = float(output.strip())
    except ValueError:
      # 변환이 불가능하면 문자열 비교 수행
      expected_val = output_val = None

    if expected_val is not None and output_val is not None:
      if not math.isclose(expected_val, output_val, rel_tol=1e-4, abs_tol=1e-4):
        raise AssertionError(
          f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
        )
    else:
      if output != expected_output:
        raise AssertionError(
          f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
        )
