from dataclasses import dataclass, field
from typing import List
from .fare_zone import FareZone
from .frame_containment_structure import FrameContainmentStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZonesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareZonesInFrame_RelStructure"

    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
