from dataclasses import dataclass
from .place_ref_structure import PlaceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceRef(PlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
