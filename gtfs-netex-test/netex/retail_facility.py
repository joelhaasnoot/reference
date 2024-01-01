from dataclasses import dataclass, field
from .retail_facility_enumeration import RetailFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RetailFacilityEnumeration = field(
        default=RetailFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
