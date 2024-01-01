from dataclasses import dataclass, field
from typing import List
from .booking_process_enumeration import BookingProcessEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingProcessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
