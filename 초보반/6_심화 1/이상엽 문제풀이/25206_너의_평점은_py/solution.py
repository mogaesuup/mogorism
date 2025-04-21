import sys

input = lambda: sys.stdin.readline().rstrip()

grade_score = {
  'A+': 4.5,
  'A0': 4.0,
  'B+': 3.5,
  'B0': 3.0,
  'C+': 2.5,
  'C0': 2.0,
  'D+': 1.5,
  'D0': 1.0,
  'F': 0.0,
}


def solve():
  sum_credit = 0
  sum_credit_time_grade = 0

  for _ in range(20):
    course, credit_text, grades = input().split()
    if grades == 'P':
      continue

    credit = float(credit_text)

    sum_credit += credit
    sum_credit_time_grade += credit * grade_score[grades]

  print(sum_credit_time_grade / sum_credit)


if __name__ == '__main__':
  solve()
