from dataclasses import dataclass
from .retail_device_security_listing_versioned_child_structure import (
    RetailDeviceSecurityListingVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceSecurityListing(
    RetailDeviceSecurityListingVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
