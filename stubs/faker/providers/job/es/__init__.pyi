from .. import Provider as BaseProvider
from ... import ElementsType as ElementsType

class Provider(BaseProvider):
    jobs: ElementsType[str]
