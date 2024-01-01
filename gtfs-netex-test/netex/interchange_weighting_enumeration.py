from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class InterchangeWeightingEnumeration(Enum):
    NO_INTERCHANGE = "noInterchange"
    INTERCHANGE_ALLOWED = "interchangeAllowed"
    RECOMMENDED_INTERCHANGE = "recommendedInterchange"
    PREFERRED_INTERCHANGE = "preferredInterchange"
