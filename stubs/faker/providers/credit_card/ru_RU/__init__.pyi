from .. import CardType as CardType, CreditCard as CreditCard, Provider as CreditCardProvider
from _typeshed import Incomplete
from faker.providers.person.ru_RU import translit as translit
from typing import Optional

class Provider(CreditCardProvider):
    prefix_visa: Incomplete
    prefix_mastercard: Incomplete
    prefix_mir: Incomplete
    prefix_maestro: Incomplete
    prefix_amex: Incomplete
    prefix_unionpay: Incomplete
    credit_card_types: Incomplete
    def credit_card_full(self, card_type: Optional[CardType] = None) -> str: ...
