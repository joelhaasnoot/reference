from dataclasses import dataclass
from .vehicle_sharing_place_assignment_version_structure import (
    VehicleSharingPlaceAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingPlaceAssignment(
    VehicleSharingPlaceAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"