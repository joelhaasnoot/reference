from dataclasses import dataclass
from .vehicle_sharing_parking_area_ref_structure import (
    VehicleSharingParkingAreaRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingParkingAreaRef(VehicleSharingParkingAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"