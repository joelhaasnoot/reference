from dataclasses import dataclass
from .usage_parameter_price_ref_structure import (
    UsageParameterPriceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameterPriceRef(UsageParameterPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
