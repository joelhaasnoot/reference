from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_part_couple import JourneyPartCouple
from netex.journey_part_couple_ref import JourneyPartCoupleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartCouplesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of JOURNEY PART COUPLEs.
    """
    class Meta:
        name = "journeyPartCouples_RelStructure"

    journey_part_couple_ref_or_journey_part_couple: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPartCoupleRef",
                    "type": JourneyPartCoupleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartCouple",
                    "type": JourneyPartCouple,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
