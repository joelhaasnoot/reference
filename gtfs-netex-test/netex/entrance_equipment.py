from dataclasses import dataclass
from .entrance_equipment_version_structure import (
    EntranceEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceEquipment(EntranceEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
