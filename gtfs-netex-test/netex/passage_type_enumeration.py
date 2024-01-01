from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PassageTypeEnumeration(Enum):
    NONE = "none"
    PATHWAY = "pathway"
    CORRIDOR = "corridor"
    OVERPASS = "overpass"
    UNDERPASS = "underpass"
    TUNNEL = "tunnel"
    OTHER = "other"
