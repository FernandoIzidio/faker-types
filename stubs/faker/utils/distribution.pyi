from random import Random
from typing import Generator, Iterable, Optional, Sequence, TypeVar

def random_sample(random: Optional[Random] = None) -> float: ...
def cumsum(it: Iterable[float]) -> Generator[float, None, None]: ...
T = TypeVar('T')

def choices_distribution_unique(a: Sequence[T], p: Optional[Sequence[float]], random: Optional[Random] = None, length: int = 1) -> Sequence[T]: ...
def choices_distribution(a: Sequence[T], p: Optional[Sequence[float]], random: Optional[Random] = None, length: int = 1) -> Sequence[T]: ...
