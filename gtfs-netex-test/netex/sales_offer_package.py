from dataclasses import dataclass
from .sales_offer_package_version_structure import (
    SalesOfferPackageVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackage(SalesOfferPackageVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
