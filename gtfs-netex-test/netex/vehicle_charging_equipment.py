from dataclasses import dataclass
from .vehicle_charging_equipment_version_structure import (
    VehicleChargingEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleChargingEquipment(VehicleChargingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
