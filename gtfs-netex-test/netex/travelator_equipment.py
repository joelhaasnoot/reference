from dataclasses import dataclass
from .travelator_equipment_version_structure import (
    TravelatorEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelatorEquipment(TravelatorEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
