from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_lines import GroupOfLines


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfLinesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfLinesInFrame_RelStructure"

    group_of_lines: List[GroupOfLines] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
