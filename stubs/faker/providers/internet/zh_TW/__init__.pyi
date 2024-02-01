from .. import Provider as InternetProvider
from _typeshed import Incomplete
from faker.utils.decorators import slugify as slugify

class Provider(InternetProvider):
    user_name_formats: Incomplete
    tlds: Incomplete
    def domain_word(self): ...
