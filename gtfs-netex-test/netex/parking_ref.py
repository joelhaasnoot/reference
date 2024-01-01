from dataclasses import dataclass
from .parking_ref_structure import ParkingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingRef(ParkingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
