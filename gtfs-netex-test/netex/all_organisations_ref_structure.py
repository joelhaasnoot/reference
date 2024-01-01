from dataclasses import dataclass, field
from .version_of_object_ref_structure import VersionOfObjectRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllOrganisationsRefStructure(VersionOfObjectRefStructure):
    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: RestrictedVar
