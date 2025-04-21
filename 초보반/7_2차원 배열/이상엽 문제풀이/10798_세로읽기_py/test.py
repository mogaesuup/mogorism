from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 테스트 케이스 1: 모든 줄의 길이가 동일한 경우
  (
    "ABCDE\n"
    "abcde\n"
    "01234\n"
    "FGHIJ\n"
    "fghij\n",
    "Aa0FfBb1GgCc2HhDd3IiEe4Jj\n"
  ),
  # 테스트 케이스 2: 각 줄의 길이가 다르게 주어진 경우
  (
    "A\n"
    "BC\n"
    "DEF\n"
    "GHIJ\n"
    "KLMNO\n",
    "ABDGKCEHLFIMJNO\n"
  ),
  # 테스트 케이스 3: 일부 줄이 빈 문자열인 경우
  (
    "\n"
    "A\n"
    "\n"
    "BC\n"
    "\n",
    "ABC\n"
  ),
  # 테스트 케이스 4: 알파벳과 숫자가 혼합된 경우
  (
    "12AB\n"
    "cdEF\n"
    "GHij\n"
    "klMN\n"
    "opQR\n",
    "1cGko2dHlpAEiMQBFjNR\n"
  ),
  # 테스트 케이스 5: 단어들이 길이가 서로 다른 경우
  (
    "HELLO\n"
    "WORLD\n"
    "TEST\n"
    "A\n"
    "BEE\n",
    "HWTABEOEELRSELLTOD\n"
  ),
  # 테스트 케이스 6: 모든 줄이 동일하며 길이가 10인 경우
  (
    "ABCDEFGHIJ\n"
    "ABCDEFGHIJ\n"
    "ABCDEFGHIJ\n"
    "ABCDEFGHIJ\n"
    "ABCDEFGHIJ\n",
    "AAAAABBBBBCCCCCDDDDDEEEEEFFFFFGGGGGHHHHHIIIIIJJJJJ\n"
  ),
  # 테스트 케이스 7: 한 줄만 길이가 길고 나머지는 짧은 경우
  (
    "X\n"
    "YZ\n"
    "12345\n"
    "abc\n"
    "!\n",
    "XY1a!Z2b3c45\n"
  ),
  # 테스트 케이스 8: 숫자와 알파벳이 혼합된 경우 (길이 다름)
  (
    "123\n"
    "abc\n"
    "45\n"
    "XYZ\n"
    "z\n",
    "1a4Xz2b5Y3cZ\n"
  ),
  # 테스트 케이스 9: 특수문자(구두점, 기호) 사용
  (
    "?!.\n"
    "*/:\n"
    ";<=\n"
    ">@?\n"
    "~`|\n",
    "?*;>~!/<@`.:=?|\n"
  ),
  # 테스트 케이스 10: 각 줄의 최대 길이(15문자)를 사용하는 경우
  (
    "ABCDEFGHIJKLMNO\n"
    "PQRSTUVWXYZABCD\n"
    "123456789012345\n"
    "098765432109876\n"
    "abcdefghijklmno\n",
    "AP10aBQ29bCR38cDS47dET56eFU65fGV74gHW83hIX92iJY01jKZ10kLA29lMB38mNC47nOD56o\n"
  ),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
