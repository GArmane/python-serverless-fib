from typing import List

def calculate_fib(limit: int) -> List[int]:
  result = [1, 1]
  for n in range(2, limit):
    result.append(result[n - 1] + result[n - 2])
  return result
