from ..la import Provider as LoremProvider
from _typeshed import Incomplete
from typing import List

class Provider(LoremProvider):
    english_word_list: Incomplete
    def english_word(self) -> str: ...
    def english_words(self, nb: int = 3, unique: bool = False) -> List[str]: ...
    def english_sentence(self, nb_words: int = 6, variable_nb_words: bool = True) -> str: ...
    def english_sentences(self, nb: int = 3) -> List[str]: ...
    def english_paragraph(self, nb_sentences: int = 3, variable_nb_sentences: bool = True) -> str: ...
    def english_paragraphs(self, nb: int = 3) -> List[str]: ...
    def english_text(self, max_nb_chars: int = 200) -> str: ...
    def english_texts(self, nb_texts: int = 3, max_nb_chars: int = 200) -> List[str]: ...
