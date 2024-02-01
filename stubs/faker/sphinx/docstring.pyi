import inspect
import logging
import re
from faker import Faker as Faker
from faker.config import AVAILABLE_LOCALES as AVAILABLE_LOCALES, DEFAULT_LOCALE as DEFAULT_LOCALE
from faker.sphinx.validator import SampleCodeValidator as SampleCodeValidator
from typing import NamedTuple
from logging import Logger

logger: Logger
DEFAULT_SAMPLE_SIZE: int
DEFAULT_SEED: int

class Sample(NamedTuple):
    size: str
    seed: str
    kwargs: str

class ProviderMethodDocstring:
    def __init__(self, app, what, name, obj, options, lines) -> None: ...
    @property
    def skipped(self): ...
    @property
    def lines(self): ...
