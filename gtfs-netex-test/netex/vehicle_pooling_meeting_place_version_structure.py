from dataclasses import dataclass
from .vehicle_meeting_place_version_structure import (
    VehicleMeetingPlaceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingMeetingPlaceVersionStructure(
    VehicleMeetingPlaceVersionStructure
):
    class Meta:
        name = "VehiclePoolingMeetingPlace_VersionStructure"