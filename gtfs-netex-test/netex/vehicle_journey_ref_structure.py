from dataclasses import dataclass
from .journey_ref_structure import JourneyRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyRefStructure(JourneyRefStructure):
    value: RestrictedVar