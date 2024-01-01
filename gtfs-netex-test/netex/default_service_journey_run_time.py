from dataclasses import dataclass
from .default_service_journey_run_time_versioned_child_structure import (
    DefaultServiceJourneyRunTimeVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultServiceJourneyRunTime(
    DefaultServiceJourneyRunTimeVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"