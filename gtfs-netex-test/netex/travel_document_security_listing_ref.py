from dataclasses import dataclass
from .travel_document_security_listing_ref_structure import (
    TravelDocumentSecurityListingRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelDocumentSecurityListingRef(
    TravelDocumentSecurityListingRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
