from dataclasses import dataclass, field
from typing import List
from .mode_ref import ModeRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "modeRefs_RelStructure"

    mode_ref: List[ModeRef] = field(
        default_factory=list,
        metadata={
            "name": "ModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
