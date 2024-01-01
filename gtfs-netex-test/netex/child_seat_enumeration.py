from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ChildSeatEnumeration(Enum):
    BABY = "baby"
    SMALL_CHILD = "smallChild"
    OLDER_CHILD = "olderChild"
    NONE = "none"
    OTHER = "other"
