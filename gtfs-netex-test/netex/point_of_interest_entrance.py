from dataclasses import dataclass
from .point_of_interest_entrance_version_structure import (
    PointOfInterestEntranceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestEntrance(PointOfInterestEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
