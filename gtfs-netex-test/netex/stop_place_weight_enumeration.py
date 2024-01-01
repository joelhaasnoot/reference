from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopPlaceWeightEnumeration(Enum):
    INTERNATIONAL = "international"
    NATIONAL = "national"
    REGIONAL = "regional"
    LOCAL = "local"
