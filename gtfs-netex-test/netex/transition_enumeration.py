from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransitionEnumeration(Enum):
    UP = "up"
    DOWN = "down"
    LEVEL = "level"
    UP_AND_DOWN = "upAndDown"
    DOWN_AND_UP = "downAndUp"
