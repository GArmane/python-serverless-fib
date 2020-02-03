from typing import List

def calculate_fib(limit: int) -> List[int]:
    result = [1, 1]
    for idx in range(2, limit):
        result.append(result[idx - 1] + result[idx - 2])
    return result
