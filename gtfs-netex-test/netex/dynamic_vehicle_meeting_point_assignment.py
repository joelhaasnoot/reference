from dataclasses import dataclass
from .dynamic_vehicle_meeting_point_assignment_version_structure import (
    DynamicVehicleMeetingPointAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicVehicleMeetingPointAssignment(
    DynamicVehicleMeetingPointAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"