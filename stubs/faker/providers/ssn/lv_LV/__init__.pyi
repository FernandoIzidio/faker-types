from .. import Provider as SsnProvider
from _typeshed import Incomplete

class Provider(SsnProvider):
    def ssn(self, min_age: int = 0, max_age: int = 105) -> str: ...
    vat_id_formats: Incomplete
    def vat_id(self) -> str: ...
