from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_retail_device_ref import TypeOfRetailDeviceRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRetailDeviceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfRetailDeviceRefs_RelStructure"

    type_of_retail_device_ref: List[TypeOfRetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
