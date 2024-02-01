from .. import Provider as GeoProvider
from _typeshed import Incomplete

class Provider(GeoProvider):
    nationalities: Incomplete
    def nationality(self) -> str: ...
