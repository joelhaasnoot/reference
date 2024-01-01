from dataclasses import dataclass
from .reselling_ref_structure import ResellingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResellingRef(ResellingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
