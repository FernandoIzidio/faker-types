from .. import Provider as PersonProvider
from _typeshed import Incomplete

class Provider(PersonProvider):
    est_rat: float
    rus_rat: Incomplete
    formats: Incomplete
    formats_male: Incomplete
    formats_female: Incomplete
    prefixes_neutral: Incomplete
    prefixes_male: Incomplete
    prefixes_female: Incomplete
    prefixes: Incomplete
    suffixes: Incomplete
    first_names_male_est: Incomplete
    first_names_female_est: Incomplete
    first_names_est: Incomplete
    first_names_male_rus: Incomplete
    first_names_female_rus: Incomplete
    first_names_rus: Incomplete
    first_names_male: Incomplete
    first_names_female: Incomplete
    first_names: Incomplete
    last_names_est: Incomplete
    last_names_rus: Incomplete
    last_names: Incomplete
    def first_name_male_est(self) -> str: ...
    def first_name_female_est(self) -> str: ...
    def first_name_male_rus(self) -> str: ...
    def first_name_female_rus(self) -> str: ...
    def first_name_est(self) -> str: ...
    def first_name_rus(self) -> str: ...
    def last_name_est(self) -> str: ...
    def last_name_rus(self) -> str: ...
