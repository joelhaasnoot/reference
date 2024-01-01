from dataclasses import dataclass
from .version_ref_structure import VersionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionRef(VersionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
