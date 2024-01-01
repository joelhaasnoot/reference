from dataclasses import dataclass
from .vehicle_meeting_point_ref_structure import (
    VehicleMeetingPointRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointRef(VehicleMeetingPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
