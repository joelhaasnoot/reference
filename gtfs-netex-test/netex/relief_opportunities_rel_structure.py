from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .relief_opportunity import ReliefOpportunity
from .relief_opportunity_ref import ReliefOpportunityRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefOpportunitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "reliefOpportunities_RelStructure"

    relief_opportunity_ref_or_relief_opportunity: List[
        Union[ReliefOpportunityRef, ReliefOpportunity]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ReliefOpportunityRef",
                    "type": ReliefOpportunityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefOpportunity",
                    "type": ReliefOpportunity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
