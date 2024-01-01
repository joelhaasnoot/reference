from dataclasses import dataclass
from .rental_availability_version_structure import (
    RentalAvailabilityVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RentalAvailability(RentalAvailabilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"