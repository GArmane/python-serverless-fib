from dataclasses import dataclass
from os import getenv

@dataclass
class Config:
    calc_limit = int(getenv('CALC_LIMIT', '10'))
