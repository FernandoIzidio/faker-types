from .. import Provider as InternetProvider
from _typeshed import Incomplete
from faker.utils.decorators import lowercase as lowercase, slugify as slugify

class Provider(InternetProvider):
    tlds: Incomplete
    safe_email_tlds = tlds
    free_email_domains: Incomplete
    email_formats: Incomplete
    def domain_word(self) -> str: ...
