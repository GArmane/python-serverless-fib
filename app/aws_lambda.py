from json import dumps
from typing import Any, Dict, Union
from app.config import Config
from app.core.fibonacci import calculate_fib

# Types
Response = Dict[str, Union[int, str]]

# Constants
CALC_LIMIT = Config().calc_limit

def _make_response(status: int, body: Any) -> Response:
    return {
        "statusCode": status,
        "body": dumps(body)
    }

def fib(_event, _context) -> Response:
    sequence = calculate_fib(CALC_LIMIT)
    return _make_response(200, sequence)
