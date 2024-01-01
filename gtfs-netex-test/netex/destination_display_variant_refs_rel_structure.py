from dataclasses import dataclass, field
from typing import List
from .destination_display_variant_ref import DestinationDisplayVariantRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariantRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "destinationDisplayVariantRefs_RelStructure"

    destination_display_variant_ref: List[
        DestinationDisplayVariantRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
