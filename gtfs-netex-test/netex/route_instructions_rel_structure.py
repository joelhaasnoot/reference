from dataclasses import dataclass, field
from typing import List
from .route_instruction import RouteInstruction
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteInstructionsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "routeInstructions_RelStructure"

    route_instruction: List[RouteInstruction] = field(
        default_factory=list,
        metadata={
            "name": "RouteInstruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
