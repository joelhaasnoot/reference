from dataclasses import dataclass
from .special_service_ref_structure import SpecialServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecialServiceRef(SpecialServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"