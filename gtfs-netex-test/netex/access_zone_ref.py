from dataclasses import dataclass
from .access_zone_ref_structure import AccessZoneRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessZoneRef(AccessZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
