from dataclasses import dataclass
from .garage_point_ref_structure import GaragePointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePointRef(GaragePointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"