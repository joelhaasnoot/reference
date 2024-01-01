from dataclasses import dataclass
from .timing_point_ref_structure import TimingPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointRefStructure(TimingPointRefStructure):
    value: RestrictedVar
