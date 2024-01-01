from dataclasses import dataclass
from .equipment_position_ref_structure import EquipmentPositionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPositionRef(EquipmentPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"