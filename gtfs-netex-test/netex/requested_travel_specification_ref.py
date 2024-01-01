from dataclasses import dataclass
from .requested_travel_specification_ref_structure import (
    RequestedTravelSpecificationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RequestedTravelSpecificationRef(
    RequestedTravelSpecificationRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
