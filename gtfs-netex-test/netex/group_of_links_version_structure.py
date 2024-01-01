from dataclasses import dataclass, field
from typing import Optional
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .link_refs_rel_structure import LinkRefsRelStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinksVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfLinks_VersionStructure"

    members: Optional[LinkRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
