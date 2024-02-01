from .. import BaseProvider as BaseProvider, ElementsType as ElementsType

localized: bool

def calculate_vin_str_weight(s: str, weight_factor: list) -> int: ...

class Provider(BaseProvider):
    license_formats: ElementsType
    def license_plate(self) -> str: ...
    def vin(self) -> str: ...
