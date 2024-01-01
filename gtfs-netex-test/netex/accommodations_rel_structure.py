from dataclasses import dataclass, field
from typing import List, Union
from .accommodation import Accommodation
from .accommodation_ref import AccommodationRef
from .containment_aggregation_structure import ContainmentAggregationStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accommodations_RelStructure"

    accommodation_ref_or_accommodation: List[
        Union[AccommodationRef, Accommodation]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccommodationRef",
                    "type": AccommodationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Accommodation",
                    "type": Accommodation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
