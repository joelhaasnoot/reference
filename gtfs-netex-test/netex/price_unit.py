from dataclasses import dataclass
from .price_unit_version_structure import PriceUnitVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceUnit(PriceUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
