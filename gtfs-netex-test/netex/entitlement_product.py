from dataclasses import dataclass
from .entitlement_product_version_structure import (
    EntitlementProductVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementProduct(EntitlementProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
