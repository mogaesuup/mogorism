from solution import solve
from util.test_runner import run_fun_solution

test_cases = [
  # 1. 단일 단어, 그룹 단어인 경우
  ('1\na\n', '1\n'),
  # 2. 단일 단어, 그룹 단어가 아닌 경우 ("aba": a가 분리되어 등장)
  ('1\naba\n', '0\n'),
  # 3. 두 단어 모두 그룹 단어인 경우
  ('2\nabc\naabb\n', '2\n'),
  # 4. 두 단어 중 하나만 그룹 단어인 경우
  ('2\naba\naabb\n', '1\n'),
  # 5. 세 단어 중 "aaa"만 그룹 단어
  ('3\nabca\naaa\naabbaa\n', '1\n'),
  # 6. 같은 문자만 연속된 경우는 그룹 단어
  ('1\ncccc\n', '1\n'),
  # 7. 5개 단어: "abc", "cba", "aaabbb"는 그룹 단어, "aba", "abab"는 아님
  ('5\nabc\ncba\naaabbb\naba\nabab\n', '3\n'),
  # 8. 4개 단어: "aabbcc", "abbbc", "aaacc"는 그룹 단어, "abcabc"는 아님
  ('4\naabbcc\nabcabc\nabbbc\naaacc\n', '3\n'),
  # 9. 단일 단어, 반복 패턴으로 그룹 단어가 아님
  ('1\nababab\n', '0\n'),
  # 10. 단일 단어, 모든 글자가 동일하므로 그룹 단어
  ('1\nzzz\n', '1\n'),
  # 11. 3개 단어 모두 내부에서 재등장하여 그룹 단어가 아님
  ('3\naba\nabba\nabbba\n', '0\n'),
  # 12. 긴 단어, 각 문자가 한 묶음으로 있는 경우
  ('1\naaabbbcccdddeee\n', '1\n'),
  # 13. 단일 단어, 문자 재등장이 분리되어 있어 그룹 단어가 아님
  ('1\nabcddc\n', '0\n'),
  # 14. 알파벳 전체가 한 번씩 등장 → 그룹 단어
  ('1\nabcdefghijklmnopqrstuvwxyz\n', '1\n'),
  # 15. 6개 단어 모두 그룹 단어인 경우
  ('6\naa\nab\nbb\nbaa\nabb\naabb\n', '6\n'),
  # 16. 2개 단어: "xyzz"는 그룹 단어, "xzyz"는 아님
  ('2\nxyzz\nxzyz\n', '1\n'),
  # 17. 길이가 1인 단어 3개 → 모두 그룹 단어
  ('3\na\nb\nc\n', '3\n'),
  # 18. 단일 단어, 처음과 끝의 문자가 분리되어 나타남
  ('1\nbaaab\n', '0\n'),
  # 19. 5개 단어: "ccca", "aaaab", "abc", "a"는 그룹 단어, "cacc"는 아님
  ('5\nccca\naaaab\nabc\na\ncacc\n', '4\n'),
  # 20. 7개 단어: "ab", "abb", "baa", "bb", "bbb"는 그룹 단어, "aba", "baba"는 아님
  ('7\nab\naba\nabb\nbaa\nbaba\nbb\nbbb\n', '5\n'),
]


def test():
  for input_data, expected_output in test_cases:
    output = run_fun_solution(input_data, solve)
    assert output == expected_output, f"Input: {input_data!r} Expected: {expected_output!r}, Got: {output!r}"
