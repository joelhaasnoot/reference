from dataclasses import dataclass
from .delivery_variant_ref_structure import DeliveryVariantRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeliveryVariantRef(DeliveryVariantRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
