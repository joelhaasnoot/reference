from dataclasses import dataclass, field
from typing import List
from .frame_containment_structure import FrameContainmentStructure
from .section_in_sequence_versioned_child_structure import FareSection


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSectionsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareSectionsInFrame_RelStructure"

    fare_section: List[FareSection] = field(
        default_factory=list,
        metadata={
            "name": "FareSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )