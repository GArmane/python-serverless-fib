import os
from typing import Dict, List, Union
from src.fibonacci import calculate_fib

Response = Dict[str, Union[int, List[int]]]


def fib(event, context) -> Response:
  max_range = int(os.getenv('CALC_LIMIT', 10))
  sequence = calculate_fib(max_range)
  return {
    "status": 200,
    "data": sequence,
  }
