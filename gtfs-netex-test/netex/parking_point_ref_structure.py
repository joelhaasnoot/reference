from dataclasses import dataclass
from .relief_point_ref_structure import ReliefPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPointRefStructure(ReliefPointRefStructure):
    value: RestrictedVar