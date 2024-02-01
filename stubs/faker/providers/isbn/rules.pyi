from _typeshed import Incomplete
from typing import Dict, List, NamedTuple

class RegistrantRule(NamedTuple):
    min: Incomplete
    max: Incomplete
    registrant_length: Incomplete

RULES: Dict[str, Dict[str, List[RegistrantRule]]]
