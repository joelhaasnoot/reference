from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SuitableEnumeration(Enum):
    SUITABLE = "suitable"
    NOT_SUITABLE = "notSuitable"
