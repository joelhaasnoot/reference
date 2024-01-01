from dataclasses import dataclass
from .wheelchair_vehicle_ref_structure import WheelchairVehicleRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WheelchairVehicleRef(WheelchairVehicleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
