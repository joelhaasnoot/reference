from dataclasses import dataclass
from .type_of_fare_product_ref_structure import TypeOfFareProductRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareProductRef(TypeOfFareProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
