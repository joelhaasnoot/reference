from dataclasses import dataclass
from .trolley_stand_equipment_ref_structure import (
    TrolleyStandEquipmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrolleyStandEquipmentRef(TrolleyStandEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
