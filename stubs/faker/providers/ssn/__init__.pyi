from .. import BaseProvider as BaseProvider, ElementsType as ElementsType

localized: bool

class Provider(BaseProvider):
    ssn_formats: ElementsType[str]
    def ssn(self) -> str: ...
