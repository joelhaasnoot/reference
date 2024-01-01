from dataclasses import dataclass
from .charging_moment_ref_structure import ChargingMomentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingMomentRef(ChargingMomentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
