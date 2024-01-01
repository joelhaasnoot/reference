from dataclasses import dataclass
from .point_of_interest_version_structure import (
    PointOfInterestVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterest(PointOfInterestVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
