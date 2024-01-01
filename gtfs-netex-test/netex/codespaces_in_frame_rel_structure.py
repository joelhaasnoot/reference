from dataclasses import dataclass, field
from typing import List
from .codespace import Codespace
from .containment_aggregation_structure import ContainmentAggregationStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CodespacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "codespacesInFrame_RelStructure"

    codespace: List[Codespace] = field(
        default_factory=list,
        metadata={
            "name": "Codespace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
