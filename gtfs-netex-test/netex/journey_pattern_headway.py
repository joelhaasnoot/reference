from dataclasses import dataclass
from .journey_pattern_headway_versioned_child_structure import (
    JourneyPatternHeadwayVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternHeadway(JourneyPatternHeadwayVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"