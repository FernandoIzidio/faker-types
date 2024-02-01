from ..en import Provider as AddressProvider
from _typeshed import Incomplete

class Provider(AddressProvider):
    counties: Incomplete
    postcode_pattern: str
    def postcode(self) -> str: ...
    def administrative_unit(self) -> str: ...
    county = administrative_unit
