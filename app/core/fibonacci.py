from typing import List

def _fib(n: int) -> int:
    if n <= 1: return n
    else: return _fib(n-1) + _fib(n-2)

def calculate_sequence(limit: int) -> List[int]:
    if limit < 0: raise ValueError('limit must be greater than 0')
    return [_fib(idx) for idx in range(limit)]
