from .. import Provider as LoremProvider
from _typeshed import Incomplete
from typing import Dict

class Provider(LoremProvider):
    word_list: Incomplete
    parts_of_speech: Dict[str, tuple]
