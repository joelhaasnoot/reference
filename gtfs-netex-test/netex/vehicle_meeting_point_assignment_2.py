from dataclasses import dataclass
from .assignment_version_structure_1 import AssignmentVersionStructure1


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointAssignment2(AssignmentVersionStructure1):
    class Meta:
        name = "VehicleMeetingPointAssignment_"
        namespace = "http://www.netex.org.uk/netex"
