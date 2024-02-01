from .. import Provider as AutomotiveProvider

class Provider(AutomotiveProvider):
    def license_plate(self) -> str: ...
