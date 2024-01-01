from dataclasses import dataclass
from .coupled_journey_ref_structure import CoupledJourneyRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CoupledJourneyRef(CoupledJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
