from dataclasses import dataclass
from .parking_point_version_structure import ParkingPointVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePointVersionStructure(ParkingPointVersionStructure):
    class Meta:
        name = "GaragePoint_VersionStructure"