from dataclasses import dataclass
from .taxi_rank_ref_structure import TaxiRankRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiRankRef(TaxiRankRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"