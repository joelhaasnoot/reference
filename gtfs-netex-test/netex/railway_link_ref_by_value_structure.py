from dataclasses import dataclass, field
from .link_ref_by_value_structure import LinkRefByValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayLinkRefByValueStructure(LinkRefByValueStructure):
    name_of_point_ref_class: str = field(
        init=False,
        default="RailwayPoint",
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        },
    )