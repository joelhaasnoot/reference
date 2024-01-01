from dataclasses import dataclass
from .rental_option_ref_structure import RentalOptionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RentalOptionRef(RentalOptionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
