from dataclasses import dataclass
from .parking_capacity_ref_structure import ParkingCapacityRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingCapacityRef(ParkingCapacityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"