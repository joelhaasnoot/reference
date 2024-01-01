from dataclasses import dataclass
from .garage_ref_structure import GarageRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GarageRef(GarageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
