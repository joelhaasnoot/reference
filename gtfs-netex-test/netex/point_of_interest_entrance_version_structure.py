from dataclasses import dataclass
from .site_entrance_version_structure import SiteEntranceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestEntranceVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "PointOfInterestEntrance_VersionStructure"
