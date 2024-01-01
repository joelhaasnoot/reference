from dataclasses import dataclass
from .point_of_interest_ref_structure import PointOfInterestRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestRef(PointOfInterestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
