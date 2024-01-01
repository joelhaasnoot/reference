from dataclasses import dataclass
from .vehicle_service_place_assignment_version_structure import (
    VehicleServicePlaceAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServicePlaceAssignment1(
    VehicleServicePlaceAssignmentVersionStructure
):
    class Meta:
        name = "VehicleServicePlaceAssignment"
        namespace = "http://www.netex.org.uk/netex"