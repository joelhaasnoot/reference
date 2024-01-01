from dataclasses import dataclass, field
from typing import List
from .reserved_space_facility_enumeration import (
    ReservedSpaceFacilityEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservedSpaceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ReservedSpaceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
