from dataclasses import dataclass
from .entitlement_required_ref_structure import EntitlementRequiredRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementRequiredRef(EntitlementRequiredRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
