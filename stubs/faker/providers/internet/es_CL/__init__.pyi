from .. import Provider as InternetProvider
from _typeshed import Incomplete
from faker.utils.decorators import lowercase as lowercase, slugify_unicode as slugify_unicode

class Provider(InternetProvider):
    safe_email_tlds: Incomplete
    tlds: Incomplete
    replacements: Incomplete
    def domain_word(self) -> str: ...
