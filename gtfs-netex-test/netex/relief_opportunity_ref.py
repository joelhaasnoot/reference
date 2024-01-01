from dataclasses import dataclass
from .relief_opportunity_ref_structure import ReliefOpportunityRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefOpportunityRef(ReliefOpportunityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
