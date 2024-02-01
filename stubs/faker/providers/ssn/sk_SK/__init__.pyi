from .. import Provider as BaseProvider
from _typeshed import Incomplete

class Provider(BaseProvider):
    vat_id_formats: Incomplete
    national_id_months: Incomplete
    def vat_id(self) -> str: ...
    def birth_number(self) -> str: ...
