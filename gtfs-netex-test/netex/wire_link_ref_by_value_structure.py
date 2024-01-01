from dataclasses import dataclass, field
from .link_ref_by_value_structure import LinkRefByValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireLinkRefByValueStructure(LinkRefByValueStructure):
    name_of_point_ref_class: str = field(
        init=False,
        default="WirePoint",
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        },
    )
