from dataclasses import dataclass, field
from typing import List
from .access_facility_enumeration import AccessFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccessFacilityEnumeration] = field(
        default_factory=lambda: [
            AccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
