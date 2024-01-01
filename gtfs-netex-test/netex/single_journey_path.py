from dataclasses import dataclass
from .single_journey_path_version_structure import (
    SingleJourneyPathVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyPath(SingleJourneyPathVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
