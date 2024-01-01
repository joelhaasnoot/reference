from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StatusEnumeration(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    OTHER = "other"