from .. import Provider as SsnProvider
from _typeshed import Incomplete

class Provider(SsnProvider):
    ssn_formats: Incomplete
    def ssn(self) -> str: ...
    def vat_id(self) -> str: ...
