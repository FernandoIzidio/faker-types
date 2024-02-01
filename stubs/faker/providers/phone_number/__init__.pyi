from .. import BaseProvider as BaseProvider, ElementsType as ElementsType

localized: bool

class Provider(BaseProvider):
    country_calling_codes: ElementsType[str]
    formats: ElementsType[str]
    msisdn_formats: ElementsType[str]
    def phone_number(self) -> str: ...
    def country_calling_code(self) -> str: ...
    def msisdn(self) -> str: ...
