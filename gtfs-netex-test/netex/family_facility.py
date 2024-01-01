from dataclasses import dataclass, field
from .family_facility_enumeration import FamilyFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FamilyFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FamilyFacilityEnumeration = field(
        default=FamilyFacilityEnumeration.NONE,
        metadata={
            "required": True,
        },
    )
