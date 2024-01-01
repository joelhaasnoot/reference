from dataclasses import dataclass, field
from typing import Optional
from .section_in_sequence_versioned_child_structure import (
    JourneyPatternVersionStructure,
)
from .service_journey_pattern_type_enumeration import (
    ServiceJourneyPatternTypeEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    class Meta:
        name = "ServiceJourneyPattern_VersionStructure"

    service_journey_pattern_type: Optional[
        ServiceJourneyPatternTypeEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )