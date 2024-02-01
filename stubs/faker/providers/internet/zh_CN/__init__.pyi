from .. import Provider as InternetProvider
from _typeshed import Incomplete
from faker.utils.decorators import slugify as slugify

class Provider(InternetProvider):
    user_name_formats: Incomplete
    tlds: Incomplete
    second_level_domains: Incomplete
    domain_formats: Incomplete
    def domain_word(self) -> str: ...
    def domain_name(self, levels: int = 1) -> str: ...
