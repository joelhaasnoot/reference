from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_zone_ref import TypeOfZoneRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfZoneRefs_RelStructure"

    type_of_zone_ref: List[TypeOfZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
