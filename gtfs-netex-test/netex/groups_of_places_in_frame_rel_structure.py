from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_places import GroupOfPlaces


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfPlacesInFrame_RelStructure"

    group_of_places: List[GroupOfPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
