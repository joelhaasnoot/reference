from dataclasses import dataclass
from .service_link_in_journey_pattern_versioned_child_structure import (
    ServiceLinkInJourneyPatternVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkInJourneyPattern(
    ServiceLinkInJourneyPatternVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
