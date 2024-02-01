from .. import Provider as BaseProvider
from _typeshed import Incomplete

class Provider(BaseProvider):
    vat_id_formats: Incomplete
    def vat_id(self) -> str: ...
