from dataclasses import dataclass
from .journey_pattern_ref_structure import JourneyPatternRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicePatternRefStructure(JourneyPatternRefStructure):
    value: RestrictedVar