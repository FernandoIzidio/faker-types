from .. import Provider as BaseProvider

def rut_check_digit(number: int) -> str: ...

class Provider(BaseProvider):
    minimum_rut_person: int
    maximum_rut_person: int
    minimum_rut_company: int
    maximum_rut_company: int
    rut_format: str
    def person_rut(self) -> str: ...
    def company_rut(self) -> str: ...
    def rut(self, min: int = ..., max: int = ...) -> str: ...