from dataclasses import dataclass
from .replacing_ref_structure import ReplacingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReplacingRef(ReplacingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
