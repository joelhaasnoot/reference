from dataclasses import dataclass, field
from typing import List, Union
from .authority import Authority
from .containment_aggregation_structure import ContainmentAggregationStructure
from .operator import Operator


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportOperatorsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transportOperatorsInFrame_RelStructure"

    authority_or_operator: List[Union[Authority, Operator]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
