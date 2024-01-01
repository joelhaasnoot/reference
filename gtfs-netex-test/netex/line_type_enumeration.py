from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LineTypeEnumeration(Enum):
    LOCAL = "local"
    URBAN = "urban"
    LONG_DISTANCE = "longDistance"
    EXPRESS = "express"
    SEASONAL = "seasonal"
    REPLACEMENT = "replacement"
    FLEXIBLE = "flexible"
    OTHER = "other"
