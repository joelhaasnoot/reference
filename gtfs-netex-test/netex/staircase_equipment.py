from dataclasses import dataclass
from .staircase_equipment_version_structure import (
    StaircaseEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StaircaseEquipment(StaircaseEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
