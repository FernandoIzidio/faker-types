from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from faker.utils.datasets import add_ordereddicts as add_ordereddicts

localized: bool

class Provider(BaseProvider):
    formats: ElementsType[str]
    first_names: ElementsType[str]
    last_names: ElementsType[str]
    language_names: ElementsType[str]
    def name(self) -> str: ...
    def first_name(self) -> str: ...
    def last_name(self) -> str: ...
    def name_male(self) -> str: ...
    def name_nonbinary(self) -> str: ...
    def name_female(self) -> str: ...
    def first_name_male(self) -> str: ...
    def first_name_nonbinary(self) -> str: ...
    def first_name_female(self) -> str: ...
    def last_name_male(self) -> str: ...
    def last_name_nonbinary(self) -> str: ...
    def last_name_female(self) -> str: ...
    def prefix(self) -> str: ...
    def prefix_male(self) -> str: ...
    def prefix_nonbinary(self) -> str: ...
    def prefix_female(self) -> str: ...
    def suffix(self) -> str: ...
    def suffix_male(self) -> str: ...
    def suffix_nonbinary(self) -> str: ...
    def suffix_female(self) -> str: ...
    def language_name(self) -> str: ...
