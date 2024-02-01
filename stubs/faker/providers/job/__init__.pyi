from .. import BaseProvider as BaseProvider, ElementsType as ElementsType

localized: bool

class Provider(BaseProvider):
    jobs: ElementsType[str]
    def job(self) -> str: ...
