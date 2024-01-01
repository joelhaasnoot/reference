from dataclasses import dataclass
from .vehicle_equipment_ref_structure import VehicleEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WheelchairVehicleRefStructure(VehicleEquipmentRefStructure):
    value: RestrictedVar
