from .. import Provider as BaseProvider
from _typeshed import Incomplete
from faker.utils import checksums as checksums

class Provider(BaseProvider):
    aadhaar_id_formats: Incomplete
    def aadhaar_id(self) -> str: ...
