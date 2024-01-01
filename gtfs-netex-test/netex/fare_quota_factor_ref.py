from dataclasses import dataclass
from .fare_quota_factor_ref_structure import FareQuotaFactorRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareQuotaFactorRef(FareQuotaFactorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"