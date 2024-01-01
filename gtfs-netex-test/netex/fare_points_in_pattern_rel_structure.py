from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_point_in_pattern import FarePointInPattern
from .fare_point_in_pattern_ref import FarePointInPatternRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FarePointsInPatternRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "farePointsInPattern_RelStructure"

    fare_point_in_pattern_ref_or_fare_point_in_pattern: List[
        Union[FarePointInPatternRef, FarePointInPattern]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FarePointInPatternRef",
                    "type": FarePointInPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePointInPattern",
                    "type": FarePointInPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
