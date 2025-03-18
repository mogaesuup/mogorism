import io
import os
import sys
from typing import Callable
import subprocess


def run_fun_solution(input_data: str, func: Callable[[], None]) -> str:
  backup_stdin = sys.stdin
  backup_stdout = sys.stdout
  try:
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    func()
    return sys.stdout.getvalue()
  finally:
    sys.stdin = backup_stdin
    sys.stdout = backup_stdout


def run_solution(input_data: str, file_path:str, file_name: str) -> str:
  result = subprocess.run(
    [sys.executable, os.path.join(os.path.dirname(file_path), file_name)],
    input=input_data,
    text=True,
    capture_output=True
  )

  return result.stdout
